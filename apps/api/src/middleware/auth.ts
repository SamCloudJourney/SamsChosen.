import type { NextFunction, Request, Response } from 'express';
import jwt from 'jsonwebtoken';
import { env } from '../config/env.js';
import { prisma, Role } from '@samchosen/db';

export interface AuthRequest extends Request {
  user?: { id: string; role: Role };
}

export async function requireAuth(req: AuthRequest, res: Response, next: NextFunction) {
  try {
    const token = req.cookies['accessToken'];
    if (!token) {
      return res.status(401).json({ error: { message: 'Unauthorized' } });
    }

    const payload = jwt.verify(token, env.JWT_SECRET) as { sub: string; role: Role };
    const activeBan = await prisma.ban.findFirst({
      where: {
        userId: payload.sub,
        OR: [{ expiresAt: null }, { expiresAt: { gt: new Date() } }],
      },
    });
    if (activeBan) {
      return res.status(403).json({ error: { message: 'Account is banned' } });
    }
    req.user = { id: payload.sub, role: payload.role };
    next();
  } catch (error) {
    return res.status(401).json({ error: { message: 'Unauthorized' } });
  }
}

export function requireAdmin(req: AuthRequest, res: Response, next: NextFunction) {
  if (!req.user || req.user.role !== Role.ADMIN) {
    return res.status(403).json({ error: { message: 'Forbidden' } });
  }
  next();
}

export async function attachUser(req: AuthRequest, _res: Response, next: NextFunction) {
  try {
    const token = req.cookies['accessToken'];
    if (!token) {
      return next();
    }
    const payload = jwt.verify(token, env.JWT_SECRET) as { sub: string; role: Role };
    const activeBan = await prisma.ban.findFirst({
      where: {
        userId: payload.sub,
        OR: [{ expiresAt: null }, { expiresAt: { gt: new Date() } }],
      },
    });
    if (activeBan) {
      return next();
    }
    req.user = { id: payload.sub, role: payload.role };
    next();
  } catch (error) {
    next();
  }
}
