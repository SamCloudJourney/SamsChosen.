import type { NextFunction, Request, Response } from 'express';

const windowMs = 60 * 1000;
const maxRequests = 60;
const store = new Map<string, { count: number; expires: number }>();

export function rateLimit(req: Request, res: Response, next: NextFunction) {
  const key = req.ip;
  const now = Date.now();
  const entry = store.get(key);

  if (!entry || entry.expires < now) {
    store.set(key, { count: 1, expires: now + windowMs });
    return next();
  }

  if (entry.count >= maxRequests) {
    return res.status(429).json({ error: { message: 'Too many requests' } });
  }

  entry.count += 1;
  store.set(key, entry);
  next();
}
