import { prisma, Role } from '@samchosen/db';
import argon2 from 'argon2';
import jwt from 'jsonwebtoken';
import { env } from '../../config/env.js';
import { generateAccessToken, generateRefreshToken } from '../../lib/token.js';
import type { RegisterInput, LoginInput } from './schema.js';
import { clearAuthCookies, setAuthCookies } from '../../lib/cookies.js';
import type { Response } from 'express';

export async function register(payload: RegisterInput, res: Response) {
  const existing = await prisma.user.findFirst({
    where: {
      OR: [{ email: payload.email }, { username: payload.username }],
    },
  });

  if (existing) {
    throw new Error('Account already exists');
  }

  const passwordHash = await argon2.hash(payload.password);
  const user = await prisma.user.create({
    data: {
      email: payload.email,
      username: payload.username,
      name: payload.name,
      passwordHash,
      areaCode: payload.areaCode.toUpperCase(),
    },
    select: {
      id: true,
      email: true,
      username: true,
      name: true,
      areaCode: true,
      role: true,
    },
  });

  const accessToken = generateAccessToken(user.id, user.role);
  const refreshToken = generateRefreshToken(user.id, user.role);
  await prisma.refreshToken.create({
    data: {
      token: refreshToken,
      userId: user.id,
      expiresAt: new Date(Date.now() + 1000 * 60 * 60 * 24 * 30),
    },
  });
  setAuthCookies(res, accessToken, refreshToken);
  return user;
}

export async function login(payload: LoginInput, res: Response) {
  const user = await prisma.user.findUnique({ where: { email: payload.email } });
  if (!user) {
    throw new Error('Invalid credentials');
  }

  const match = await argon2.verify(user.passwordHash, payload.password);
  if (!match) {
    throw new Error('Invalid credentials');
  }

  const accessToken = generateAccessToken(user.id, user.role);
  const refreshToken = generateRefreshToken(user.id, user.role);
  await prisma.refreshToken.create({
    data: {
      token: refreshToken,
      userId: user.id,
      expiresAt: new Date(Date.now() + 1000 * 60 * 60 * 24 * 30),
    },
  });
  setAuthCookies(res, accessToken, refreshToken);

  const { passwordHash, ...safeUser } = user;
  return safeUser;
}

export async function refresh(res: Response, token?: string) {
  if (!token) {
    throw new Error('Missing refresh token');
  }
  const stored = await prisma.refreshToken.findUnique({ where: { token } });
  if (!stored || stored.expiresAt < new Date() || stored.revoked) {
    throw new Error('Invalid refresh token');
  }
  const payload = jwt.verify(token, env.JWT_REFRESH_SECRET) as { sub: string; role: Role };
  const accessToken = generateAccessToken(payload.sub, payload.role);
  const refreshToken = generateRefreshToken(payload.sub, payload.role);
  await prisma.refreshToken.update({
    where: { token },
    data: { revoked: true },
  });
  await prisma.refreshToken.create({
    data: {
      token: refreshToken,
      userId: payload.sub,
      expiresAt: new Date(Date.now() + 1000 * 60 * 60 * 24 * 30),
    },
  });
  setAuthCookies(res, accessToken, refreshToken);
  return { accessToken, refreshToken };
}

export async function logout(res: Response, token?: string) {
  if (token) {
    await prisma.refreshToken.updateMany({
      where: { token },
      data: { revoked: true },
    });
  }
  clearAuthCookies(res);
}
