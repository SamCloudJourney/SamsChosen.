import { Router } from 'express';
import { requireAdmin, requireAuth, type AuthRequest } from '../../middleware/auth.js';
import { captchaGuard } from '../../middleware/captcha.js';
import { createThreadSchema } from './schema.js';
import { createThread, getThread, listLatestThreads, toggleLock, togglePin } from './service.js';

export const threadRouter = Router();

threadRouter.get('/', async (_req, res, next) => {
  try {
    const threads = await listLatestThreads();
    res.json({ threads });
  } catch (error) {
    next(error);
  }
});

threadRouter.get('/:id', async (req, res, next) => {
  try {
    const thread = await getThread(req.params.id);
    if (!thread) {
      return res.status(404).json({ error: { message: 'Thread not found' } });
    }
    res.json({ thread });
  } catch (error) {
    next(error);
  }
});

threadRouter.post('/', requireAuth, captchaGuard, async (req: AuthRequest, res, next) => {
  try {
    const payload = createThreadSchema.parse(req.body);
    const thread = await createThread(req.user!.id, payload);
    res.status(201).json({ thread });
  } catch (error) {
    next(error);
  }
});

threadRouter.post('/:id/pin', requireAuth, requireAdmin, async (req, res, next) => {
  try {
    const thread = await togglePin(req.params.id, true);
    res.json({ thread });
  } catch (error) {
    next(error);
  }
});

threadRouter.post('/:id/unpin', requireAuth, requireAdmin, async (req, res, next) => {
  try {
    const thread = await togglePin(req.params.id, false);
    res.json({ thread });
  } catch (error) {
    next(error);
  }
});

threadRouter.post('/:id/lock', requireAuth, requireAdmin, async (req, res, next) => {
  try {
    const thread = await toggleLock(req.params.id, true);
    res.json({ thread });
  } catch (error) {
    next(error);
  }
});

threadRouter.post('/:id/unlock', requireAuth, requireAdmin, async (req, res, next) => {
  try {
    const thread = await toggleLock(req.params.id, false);
    res.json({ thread });
  } catch (error) {
    next(error);
  }
});
