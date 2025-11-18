import { Router } from 'express';
import { requireAuth, type AuthRequest } from '../../middleware/auth.js';
import { updateProfileSchema } from './schema.js';
import { getPublicProfile, updateProfile } from './service.js';

export const userRouter = Router();

userRouter.get('/:username', async (req, res, next) => {
  try {
    const profile = await getPublicProfile(req.params.username);
    if (!profile) {
      return res.status(404).json({ error: { message: 'User not found' } });
    }
    res.json({ profile });
  } catch (error) {
    next(error);
  }
});

userRouter.patch('/me', requireAuth, async (req: AuthRequest, res, next) => {
  try {
    const payload = updateProfileSchema.parse(req.body);
    const profile = await updateProfile(req.user!.id, payload);
    res.json({ profile });
  } catch (error) {
    next(error);
  }
});
