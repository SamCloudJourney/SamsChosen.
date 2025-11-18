import { Router } from 'express';
import { requireAuth, type AuthRequest } from '../../middleware/auth.js';
import { notificationsQuerySchema } from './schema.js';
import { listNotifications, markRead } from './service.js';

export const notificationRouter = Router();

notificationRouter.get('/', requireAuth, async (req: AuthRequest, res, next) => {
  try {
    const query = notificationsQuerySchema.parse(req.query);
    const since = query.since ? new Date(query.since) : undefined;
    const notifications = await listNotifications(req.user!.id, since);
    res.json({ notifications });
  } catch (error) {
    next(error);
  }
});

notificationRouter.post('/:id/read', requireAuth, async (req: AuthRequest, res, next) => {
  try {
    await markRead(req.user!.id, req.params.id);
    res.status(204).send();
  } catch (error) {
    next(error);
  }
});
