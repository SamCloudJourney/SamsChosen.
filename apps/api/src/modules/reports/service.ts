import { prisma, ReportStatus } from '@samchosen/db';
import type { CreateReportInput } from './schema.js';

export function createReport(reporterId: string, payload: CreateReportInput) {
  if (!payload.threadId && !payload.postId) {
    throw new Error('Thread or post must be provided');
  }
  return prisma.report.create({
    data: {
      reporterId,
      reason: payload.reason,
      threadId: payload.threadId,
      postId: payload.postId,
    },
  });
}

export function listReports() {
  return prisma.report.findMany({
    orderBy: { createdAt: 'desc' },
    take: 50,
    include: {
      reporter: { select: { username: true, areaCode: true } },
      thread: { select: { title: true } },
      post: { select: { content: true } },
    },
  });
}

export function updateReportStatus(reportId: string, status: ReportStatus) {
  return prisma.report.update({
    where: { id: reportId },
    data: { status, resolvedAt: new Date() },
  });
}
