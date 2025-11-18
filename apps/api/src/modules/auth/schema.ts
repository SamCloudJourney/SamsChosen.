import { z } from 'zod';

export const registerSchema = z.object({
  email: z.string().email(),
  username: z.string().min(3).max(32),
  name: z.string().min(2).max(80),
  password: z.string().min(8).max(128),
  areaCode: z.string().regex(/^SE(15|22)$/i, 'Area must be SE15 or SE22'),
});

export const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8).max(128),
});

export type RegisterInput = z.infer<typeof registerSchema>;
export type LoginInput = z.infer<typeof loginSchema>;
