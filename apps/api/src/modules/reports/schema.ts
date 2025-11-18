import { z } from 'zod';

export const createReportSchema = z.object({
  reason: z.string().min(5).max(500),
  threadId: z.string().cuid().optional(),
  postId: z.string().cuid().optional(),
});

export type CreateReportInput = z.infer<typeof createReportSchema>;
