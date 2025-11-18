import { Router } from 'express';
import { requireAuth, type AuthRequest } from '../../middleware/auth.js';
import { createReportSchema } from './schema.js';
import { createReport } from './service.js';

export const reportRouter = Router();

reportRouter.post('/', requireAuth, async (req: AuthRequest, res, next) => {
  try {
    const payload = createReportSchema.parse(req.body);
    const report = await createReport(req.user!.id, payload);
    res.status(201).json({ report });
  } catch (error) {
    next(error);
  }
});
