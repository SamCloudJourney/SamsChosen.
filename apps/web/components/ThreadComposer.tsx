'use client';

import { useState } from 'react';
import { apiFetch } from '../lib/api-client';
import type { Category } from '../lib/types';
import { z } from 'zod';
import { logClientError } from '../lib/monitoring';

const composerSchema = z.object({
  title: z.string().min(5),
  content: z.string().min(10),
  categoryId: z.string().min(1),
});

interface Props {
  categories: Category[];
}

export function ThreadComposer({ categories }: Props) {
  const [formState, setFormState] = useState({ title: '', content: '', categoryId: categories[0]?.id ?? '' });
  const [status, setStatus] = useState<'idle' | 'submitting' | 'success' | 'error'>('idle');
  const [error, setError] = useState<string | null>(null);
  const disabled = categories.length === 0;

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const parsed = composerSchema.safeParse(formState);
    if (!parsed.success) {
      setError(parsed.error.errors[0]?.message || 'Invalid form');
      return;
    }

    setStatus('submitting');
    setError(null);
    try {
      await apiFetch('/threads', {
        method: 'POST',
        body: parsed.data,
      });
      setStatus('success');
      setFormState({ title: '', content: '', categoryId: categories[0]?.id ?? '' });
    } catch (err) {
      setStatus('error');
      setError(err instanceof Error ? err.message : 'Failed to create thread');
      if (err instanceof Error) {
        logClientError(err);
      }
    }
  }

  return (
    <form onSubmit={handleSubmit} className="rounded-2xl border border-dashed border-slate-300 bg-white p-5 shadow-inner">
      <div className="flex flex-col gap-3">
        <div>
          <label className="text-xs font-semibold uppercase text-slate-500">Title</label>
          <input
            className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2"
            value={formState.title}
            onChange={(event) => setFormState({ ...formState, title: event.target.value })}
            placeholder="Start a new neighbourhood chat"
          />
        </div>
        <div>
          <label className="text-xs font-semibold uppercase text-slate-500">Category</label>
          <select
            className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2"
            value={formState.categoryId}
            onChange={(event) => setFormState({ ...formState, categoryId: event.target.value })}
          >
            {categories.map((category) => (
              <option key={category.id} value={category.id}>
                {category.name}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label className="text-xs font-semibold uppercase text-slate-500">What&apos;s happening?</label>
          <textarea
            className="mt-1 min-h-[120px] w-full rounded-xl border border-slate-200 px-3 py-2"
            value={formState.content}
            onChange={(event) => setFormState({ ...formState, content: event.target.value })}
          />
        </div>
        {error && <p className="text-sm text-rose-600">{error}</p>}
        <button
          type="submit"
          className="inline-flex items-center justify-center rounded-full bg-brand-600 px-5 py-2 text-white disabled:cursor-not-allowed disabled:opacity-50"
          disabled={status === 'submitting' || disabled}
        >
          {disabled ? 'No categories yet' : status === 'submitting' ? 'Posting…' : 'Post thread'}
        </button>
        {status === 'success' && <p className="text-sm text-emerald-600">Thread created! Refresh to view.</p>}
      </div>
    </form>
  );
}
