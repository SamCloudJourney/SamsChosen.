import { z } from 'zod';

export const createThreadSchema = z.object({
  title: z.string().min(5).max(180),
  content: z.string().min(10),
  categoryId: z.string().cuid(),
  price: z.number().int().nonnegative().optional(),
  location: z.string().max(120).optional(),
});

export type CreateThreadInput = z.infer<typeof createThreadSchema>;
