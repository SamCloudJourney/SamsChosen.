import type { NextFunction, Request, Response } from 'express';
import { env } from '../config/env.js';

export function captchaGuard(req: Request, res: Response, next: NextFunction) {
  if (!env.CAPTCHA_SECRET) {
    return next();
  }
  const answer = req.headers['x-captcha-answer'];
  if (answer !== env.CAPTCHA_SECRET) {
    return res.status(400).json({ error: { message: 'Captcha required' } });
  }
  next();
}
