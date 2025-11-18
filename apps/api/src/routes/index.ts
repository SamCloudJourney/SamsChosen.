import { Router } from 'express';
import { authRouter } from '../modules/auth/router.js';
import { userRouter } from '../modules/users/router.js';
import { categoryRouter } from '../modules/categories/router.js';
import { threadRouter } from '../modules/threads/router.js';
import { postRouter } from '../modules/posts/router.js';
import { notificationRouter } from '../modules/notifications/router.js';
import { reportRouter } from '../modules/reports/router.js';
import { adminRouter } from '../modules/admin/router.js';
import { searchRouter } from '../modules/search/router.js';
import { attachUser } from '../middleware/auth.js';
import { rateLimit } from '../middleware/rate-limit.js';

const router = Router();

router.use(rateLimit);
router.use(attachUser);
router.use('/auth', authRouter);
router.use('/users', userRouter);
router.use('/categories', categoryRouter);
router.use('/threads', threadRouter);
router.use('/posts', postRouter);
router.use('/notifications', notificationRouter);
router.use('/reports', reportRouter);
router.use('/admin', adminRouter);
router.use('/search', searchRouter);

export default router;
