import { Router } from 'express';
import { z } from 'zod';
import { prisma } from '@samchosen/db';

const searchQuerySchema = z.object({
  query: z.string().min(2),
  categoryId: z.string().cuid().optional(),
  area: z.string().optional(),
});

export const searchRouter = Router();

searchRouter.get('/', async (req, res, next) => {
  try {
    const query = searchQuerySchema.parse(req.query);
    const threads = await prisma.thread.findMany({
      where: {
        title: { contains: query.query, mode: 'insensitive' },
        ...(query.categoryId ? { categoryId: query.categoryId } : {}),
        ...(query.area
          ? {
              author: {
                areaCode: query.area.toUpperCase(),
              },
            }
          : {}),
      },
      take: 20,
      include: {
        category: true,
        author: { select: { username: true, areaCode: true } },
        _count: { select: { posts: true } },
      },
    });
    res.json({ threads });
  } catch (error) {
    next(error);
  }
});
