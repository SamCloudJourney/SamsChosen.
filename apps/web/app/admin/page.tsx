import { apiFetch } from '../../lib/api-client';
import type { Category } from '../../lib/types';

export default async function AdminPage() {
  const { categories } = await apiFetch<{ categories: Category[] }>('/categories');
  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-2xl font-semibold text-slate-900">Admin overview</h1>
        <p className="text-sm text-slate-600">Quick stats to monitor the community.</p>
      </div>
      <div className="grid gap-4 md:grid-cols-3">
        {categories.map((category) => (
          <div key={category.id} className="rounded-2xl border border-slate-200 bg-white p-4 shadow-sm">
            <p className="text-xs uppercase text-slate-500">Category</p>
            <p className="text-lg font-semibold text-slate-900">{category.name}</p>
            <p className="text-sm text-slate-500">Slug: {category.slug}</p>
          </div>
        ))}
      </div>
      <p className="text-xs text-slate-500">
        Moderation queues live in the admin API. Use the backend dashboard or API client to resolve reports.
      </p>
    </div>
  );
}
