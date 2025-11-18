import { z } from 'zod';

export const notificationsQuerySchema = z.object({
  since: z.string().datetime().optional(),
});
