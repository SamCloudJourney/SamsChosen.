import { Router } from 'express';
import { loginSchema, registerSchema } from './schema.js';
import { login, logout, refresh, register } from './service.js';
import { captchaGuard } from '../../middleware/captcha.js';

export const authRouter = Router();

authRouter.post('/register', captchaGuard, async (req, res, next) => {
  try {
    const payload = registerSchema.parse(req.body);
    const user = await register(payload, res);
    res.status(201).json({ user });
  } catch (error) {
    next(error);
  }
});

authRouter.post('/login', async (req, res, next) => {
  try {
    const payload = loginSchema.parse(req.body);
    const user = await login(payload, res);
    res.json({ user });
  } catch (error) {
    next(error);
  }
});

authRouter.post('/refresh', async (req, res, next) => {
  try {
    const token = req.cookies['refreshToken'];
    const tokens = await refresh(res, token);
    res.json(tokens);
  } catch (error) {
    next(error);
  }
});

authRouter.post('/logout', async (req, res, next) => {
  try {
    const token = req.cookies['refreshToken'];
    await logout(res, token);
    res.status(204).send();
  } catch (error) {
    next(error);
  }
});
