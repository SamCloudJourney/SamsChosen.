import { prisma } from '@samchosen/db';
import type { CreatePostInput } from './schema.js';

const mentionRegex = /@([a-zA-Z0-9_]+)/g;
const bannedPhrases = ['spam link', 'buy now'];

export function extractMentions(content: string) {
  const matches = content.matchAll(mentionRegex);
  return Array.from(new Set(Array.from(matches, (m) => m[1])));
}

export async function createPost(authorId: string, payload: CreatePostInput) {
  const normalized = payload.content.toLowerCase();
  if (bannedPhrases.some((phrase) => normalized.includes(phrase))) {
    throw new Error('Content violates community rules');
  }
  const mentions = extractMentions(payload.content);
  return prisma.post.create({
    data: {
      threadId: payload.threadId,
      authorId,
      content: payload.content,
      parentId: payload.parentId,
      mentions,
    },
  });
}
