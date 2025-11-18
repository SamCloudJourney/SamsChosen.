import type { NextFetchRequestConfig } from 'next/dist/server/web/spec-extension/request';

export type HttpMethod = 'GET' | 'POST' | 'PATCH';

interface FetchOptions<T> {
  method?: HttpMethod;
  body?: T;
  cache?: RequestCache;
  next?: NextFetchRequestConfig;
}

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:4000/api';

export async function apiFetch<R, B = unknown>(path: string, options: FetchOptions<B> = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    method: options.method ?? 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
    body: options.body ? JSON.stringify(options.body) : undefined,
    cache: options.cache ?? 'no-store',
    next: options.next,
    credentials: 'include',
  });

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    throw new Error(errorBody?.error?.message || 'Request failed');
  }

  return (await response.json()) as R;
}
