import { apiFetch } from '../../../lib/api-client';
import type { Category, Thread } from '../../../lib/types';
import { ThreadCard } from '../../../components/ThreadCard';

interface Props {
  params: { slug: string };
}

export default async function CategoryPage({ params }: Props) {
  const data = await apiFetch<{ category: Category & { threads: Thread[] } }>(`/categories/${params.slug}`);
  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs uppercase tracking-[0.25em] text-slate-500">Category</p>
        <h1 className="text-3xl font-semibold text-slate-900">{data.category.name}</h1>
        <p className="text-sm text-slate-600">{data.category.description}</p>
      </div>
      <div className="space-y-4">
        {data.category.threads.map((thread) => (
          <ThreadCard key={thread.id} thread={thread} />
        ))}
      </div>
    </div>
  );
}
