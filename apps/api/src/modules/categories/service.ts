import { prisma } from '@samchosen/db';

export function listCategories() {
  return prisma.category.findMany({
    orderBy: { name: 'asc' },
  });
}

export function getCategoryWithThreads(slug: string) {
  return prisma.category.findUnique({
    where: { slug },
    include: {
      threads: {
        orderBy: { updatedAt: 'desc' },
        take: 25,
        include: {
          category: true,
          author: {
            select: { username: true, areaCode: true },
          },
          _count: { select: { posts: true } },
        },
      },
    },
  });
}
