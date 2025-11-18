'use client';

import type { Notification } from '../lib/types';

interface Props {
  notifications: Notification[];
}

export function NotificationList({ notifications }: Props) {
  if (notifications.length === 0) {
    return <p className="text-sm text-slate-500">You&apos;re all caught up.</p>;
  }

  return (
    <ul className="space-y-3">
      {notifications.map((notification) => (
        <li key={notification.id} className="rounded-xl border border-slate-200 bg-white p-4">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-slate-900">{notification.type}</p>
              <p className="text-xs text-slate-500">
                {new Date(notification.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
              </p>
            </div>
            {!notification.readAt && <span className="text-xs font-semibold text-brand-500">New</span>}
          </div>
        </li>
      ))}
    </ul>
  );
}
