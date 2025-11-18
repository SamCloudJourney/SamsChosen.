import { prisma } from '@samchosen/db';
import type { UpdateProfileInput } from './schema.js';

export function getPublicProfile(username: string) {
  return prisma.user.findUnique({
    where: { username },
    select: {
      id: true,
      username: true,
      name: true,
      bio: true,
      avatarUrl: true,
      areaCode: true,
      createdAt: true,
      threads: {
        select: {
          id: true,
          title: true,
          createdAt: true,
          updatedAt: true,
          content: true,
          category: true,
          author: { select: { username: true, areaCode: true } },
          _count: { select: { posts: true } },
          price: true,
          location: true,
        },
        take: 10,
        orderBy: { createdAt: 'desc' },
      },
    },
  });
}

export function updateProfile(userId: string, payload: UpdateProfileInput) {
  return prisma.user.update({
    where: { id: userId },
    data: payload,
    select: {
      id: true,
      username: true,
      name: true,
      bio: true,
      avatarUrl: true,
      areaCode: true,
    },
  });
}
