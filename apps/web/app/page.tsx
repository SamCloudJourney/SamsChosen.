import { apiFetch } from '../lib/api-client';
import type { Category, Thread } from '../lib/types';
import { CategoryGrid } from '../components/CategoryGrid';
import { ThreadCard } from '../components/ThreadCard';
import { ThreadComposer } from '../components/ThreadComposer';

async function getHomeData() {
  const [{ categories }, { threads }] = await Promise.all([
    apiFetch<{ categories: Category[] }>('/categories', { cache: 'no-store' }),
    apiFetch<{ threads: Thread[] }>('/threads', { cache: 'no-store' }),
  ]);
  return { categories, threads };
}

export default async function HomePage() {
  const { categories, threads } = await getHomeData();
  return (
    <div className="space-y-10">
      <section>
        <h2 className="text-2xl font-semibold text-slate-900">Neighbourhood threads</h2>
        <p className="text-sm text-slate-600">Fresh discussions from SE22 & SE15.</p>
        <div className="mt-6 grid gap-4">
          {threads.map((thread) => (
            <ThreadCard key={thread.id} thread={thread} />
          ))}
        </div>
      </section>
      <section className="grid gap-8 lg:grid-cols-[2fr,1fr]">
        <div className="space-y-4">
          <h2 className="text-xl font-semibold text-slate-900">Start a thread</h2>
          <ThreadComposer categories={categories} />
        </div>
        <div>
          <h2 className="text-xl font-semibold text-slate-900">Explore categories</h2>
          <p className="text-sm text-slate-600">Everything happening locally.</p>
          <div className="mt-4">
            <CategoryGrid categories={categories} />
          </div>
        </div>
      </section>
    </div>
  );
}
