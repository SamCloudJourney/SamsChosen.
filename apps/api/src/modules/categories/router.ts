import { Router } from 'express';
import { getCategoryWithThreads, listCategories } from './service.js';

export const categoryRouter = Router();

categoryRouter.get('/', async (_req, res, next) => {
  try {
    const categories = await listCategories();
    res.json({ categories });
  } catch (error) {
    next(error);
  }
});

categoryRouter.get('/:slug', async (req, res, next) => {
  try {
    const category = await getCategoryWithThreads(req.params.slug);
    if (!category) {
      return res.status(404).json({ error: { message: 'Category not found' } });
    }
    res.json({ category });
  } catch (error) {
    next(error);
  }
});
