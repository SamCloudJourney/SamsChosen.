import { z } from 'zod';

export const createPostSchema = z.object({
  threadId: z.string().cuid(),
  content: z.string().min(2),
  parentId: z.string().cuid().optional(),
});

export type CreatePostInput = z.infer<typeof createPostSchema>;
