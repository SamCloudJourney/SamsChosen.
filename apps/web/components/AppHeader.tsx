import Link from 'next/link';
import { MapPin, BellRing } from 'lucide-react';
import { Suspense } from 'react';
import { NotificationBell } from './NotificationBell';

export function AppHeader() {
  return (
    <header className="border-b border-slate-200 bg-white">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <Link href="/" className="text-xl font-semibold text-brand-600">
          East Dulwich Forum
        </Link>
        <nav className="flex items-center gap-4 text-sm text-slate-600">
          <Link href="/categories/general">Categories</Link>
          <Link href="/search">Search</Link>
          <Link href="/admin" className="font-medium">
            Admin
          </Link>
          <span className="inline-flex items-center text-xs font-semibold text-brand-600">
            <MapPin className="mr-1 h-4 w-4" /> SE22 · SE15
          </span>
          <Suspense fallback={<BellRing className="h-5 w-5 text-slate-400" />}>
            <NotificationBell />
          </Suspense>
        </nav>
      </div>
    </header>
  );
}
