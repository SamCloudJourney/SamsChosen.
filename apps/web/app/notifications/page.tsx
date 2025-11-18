import { NotificationsClient } from '../../components/NotificationsClient';

export default function NotificationsPage() {
  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-2xl font-semibold text-slate-900">Notifications</h1>
        <p className="text-sm text-slate-600">Polling every 15 seconds for new replies and mentions.</p>
      </div>
      <NotificationsClient />
    </div>
  );
}
