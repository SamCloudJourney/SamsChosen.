import { Router } from 'express';
import { createPostSchema } from './schema.js';
import { createPost } from './service.js';
import { requireAuth, type AuthRequest } from '../../middleware/auth.js';
import { captchaGuard } from '../../middleware/captcha.js';

export const postRouter = Router();

postRouter.post('/', requireAuth, captchaGuard, async (req: AuthRequest, res, next) => {
  try {
    const payload = createPostSchema.parse(req.body);
    const post = await createPost(req.user!.id, payload);
    res.status(201).json({ post });
  } catch (error) {
    next(error);
  }
});
