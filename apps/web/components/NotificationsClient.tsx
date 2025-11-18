'use client';

import { useQuery } from '@tanstack/react-query';
import { apiFetch } from '../lib/api-client';
import type { Notification } from '../lib/types';
import { NotificationList } from './NotificationList';

async function fetchNotifications() {
  const response = await apiFetch<{ notifications: Notification[] }>('/notifications');
  return response.notifications;
}

export function NotificationsClient() {
  const { data, isLoading } = useQuery({
    queryKey: ['notifications-page'],
    queryFn: fetchNotifications,
    refetchInterval: 15000,
  });

  if (isLoading) {
    return <p className="text-sm text-slate-500">Loading notifications…</p>;
  }

  return <NotificationList notifications={data ?? []} />;
}
