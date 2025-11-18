import { prisma, ReportStatus } from '@samchosen/db';

export const adminService = {
  listReports: () =>
    prisma.report.findMany({
      orderBy: { createdAt: 'desc' },
      include: {
        reporter: { select: { username: true } },
        thread: { select: { title: true } },
        post: { select: { content: true } },
      },
    }),
  updateReport: (reportId: string, status: ReportStatus) =>
    prisma.report.update({
      where: { id: reportId },
      data: { status, resolvedAt: new Date() },
    }),
  banUser: (userId: string, reason: string, expiresAt?: Date) =>
    prisma.ban.create({
      data: { userId, reason, expiresAt },
    }),
};
