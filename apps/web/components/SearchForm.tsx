'use client';

import { useState } from 'react';
import { apiFetch } from '../lib/api-client';
import type { Thread } from '../lib/types';
import { ThreadCard } from './ThreadCard';

export function SearchForm() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<Thread[]>([]);
  const [isSearching, setSearching] = useState(false);

  async function handleSearch(event: React.FormEvent) {
    event.preventDefault();
    setSearching(true);
    try {
      const response = await apiFetch<{ threads: Thread[] }>(`/search?query=${encodeURIComponent(query)}`);
      setResults(response.threads);
    } catch (error) {
      console.error(error);
    } finally {
      setSearching(false);
    }
  }

  return (
    <div className="space-y-6">
      <form onSubmit={handleSearch} className="flex gap-3">
        <input
          className="flex-1 rounded-full border border-slate-200 px-4 py-2"
          placeholder="Search SE22 & SE15 conversations"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
        />
        <button className="rounded-full bg-brand-600 px-5 py-2 text-white" disabled={isSearching}>
          {isSearching ? 'Searching…' : 'Search'}
        </button>
      </form>
      <div className="space-y-4">
        {results.map((thread) => (
          <ThreadCard key={thread.id} thread={thread} />
        ))}
      </div>
    </div>
  );
}
