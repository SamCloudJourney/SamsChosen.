'use client';

import { useQuery } from '@tanstack/react-query';
import { BellRing } from 'lucide-react';
import Link from 'next/link';
import { apiFetch } from '../lib/api-client';
import type { Notification } from '../lib/types';

async function fetchNotifications() {
  const response = await apiFetch<{ notifications: Notification[] }>('/notifications');
  return response.notifications;
}

export function NotificationBell() {
  const { data } = useQuery({
    queryKey: ['notifications'],
    queryFn: fetchNotifications,
    refetchInterval: 15000,
  });

  const unread = data?.filter((notification) => !notification.readAt).length ?? 0;

  return (
    <Link href="/notifications" className="relative inline-flex">
      <BellRing className="h-5 w-5 text-slate-600" />
      {unread > 0 && (
        <span className="absolute -right-1 -top-1 inline-flex h-4 min-w-[1rem] items-center justify-center rounded-full bg-brand-500 px-1 text-[10px] font-semibold text-white">
          {unread}
        </span>
      )}
    </Link>
  );
}
