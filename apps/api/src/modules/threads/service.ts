import { prisma } from '@samchosen/db';
import type { CreateThreadInput } from './schema.js';

export function listLatestThreads() {
  return prisma.thread.findMany({
    orderBy: { updatedAt: 'desc' },
    take: 25,
    include: {
      category: true,
      author: { select: { username: true, areaCode: true } },
      _count: { select: { posts: true } },
    },
  });
}

export function getThread(threadId: string) {
  return prisma.thread.findUnique({
    where: { id: threadId },
    include: {
      author: { select: { username: true, areaCode: true, avatarUrl: true } },
      category: true,
      posts: {
        include: {
          author: { select: { username: true, areaCode: true, avatarUrl: true } },
        },
        orderBy: { createdAt: 'asc' },
      },
    },
  });
}

export function createThread(authorId: string, payload: CreateThreadInput) {
  return prisma.thread.create({
    data: {
      title: payload.title,
      content: payload.content,
      categoryId: payload.categoryId,
      authorId,
      price: payload.price,
      location: payload.location,
    },
  });
}

export function togglePin(threadId: string, pinned: boolean) {
  return prisma.thread.update({
    where: { id: threadId },
    data: { pinned },
  });
}

export function toggleLock(threadId: string, locked: boolean) {
  return prisma.thread.update({
    where: { id: threadId },
    data: { locked },
  });
}
