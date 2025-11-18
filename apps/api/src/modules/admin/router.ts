import { Router } from 'express';
import { requireAdmin, requireAuth } from '../../middleware/auth.js';
import { adminService } from './service.js';
import { z } from 'zod';
import { ReportStatus } from '@samchosen/db';

export const adminRouter = Router();

adminRouter.use(requireAuth, requireAdmin);

adminRouter.get('/reports', async (_req, res, next) => {
  try {
    const reports = await adminService.listReports();
    res.json({ reports });
  } catch (error) {
    next(error);
  }
});

adminRouter.post('/reports/:id', async (req, res, next) => {
  try {
    const body = z
      .object({ status: z.nativeEnum(ReportStatus) })
      .parse(req.body);
    const report = await adminService.updateReport(req.params.id, body.status);
    res.json({ report });
  } catch (error) {
    next(error);
  }
});

adminRouter.post('/bans', async (req, res, next) => {
  try {
    const body = z
      .object({ userId: z.string().cuid(), reason: z.string().min(5), expiresAt: z.string().datetime().optional() })
      .parse(req.body);
    const ban = await adminService.banUser(
      body.userId,
      body.reason,
      body.expiresAt ? new Date(body.expiresAt) : undefined
    );
    res.status(201).json({ ban });
  } catch (error) {
    next(error);
  }
});
