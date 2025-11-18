import './globals.css';
import type { Metadata } from 'next';
import { AppProviders } from '../components/providers';
import { AppHeader } from '../components/AppHeader';

export const metadata: Metadata = {
  title: 'East Dulwich Forum',
  description: 'Neighbour-first discussions for SE22 & SE15.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <AppProviders>
          <div className="min-h-screen bg-slate-50">
            <AppHeader />
            <main className="mx-auto max-w-6xl px-6 py-8">{children}</main>
          </div>
        </AppProviders>
      </body>
    </html>
  );
}
