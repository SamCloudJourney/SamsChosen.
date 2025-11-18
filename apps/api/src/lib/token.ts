import jwt from 'jsonwebtoken';
import { env } from '../config/env.js';
import type { Role } from '@samchosen/db';

export interface TokenPair {
  accessToken: string;
  refreshToken: string;
}

export function generateAccessToken(userId: string, role: Role) {
  return jwt.sign({ role }, env.JWT_SECRET, {
    subject: userId,
    expiresIn: '15m',
  });
}

export function generateRefreshToken(userId: string, role: Role) {
  return jwt.sign({ role }, env.JWT_REFRESH_SECRET, {
    subject: userId,
    expiresIn: '30d',
  });
}
