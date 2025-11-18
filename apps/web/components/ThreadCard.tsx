'use client';

import Link from 'next/link';
import { MapPin } from 'lucide-react';
import type { Thread } from '../lib/types';
import { AreaBadge } from './AreaBadge';

interface Props {
  thread: Thread;
}

export function ThreadCard({ thread }: Props) {
  return (
    <article className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
      <div className="flex items-start justify-between">
        <div>
          <Link href={`/threads/${thread.id}`} className="text-lg font-semibold text-slate-900">
            {thread.title}
          </Link>
          <p className="mt-1 text-sm text-slate-600 line-clamp-2">{thread.content}</p>
        </div>
        <AreaBadge area={thread.author.areaCode} />
      </div>
      <div className="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-500">
        <span>by @{thread.author.username}</span>
        <span>· {new Date(thread.updatedAt).toLocaleDateString()}</span>
        {thread.location && (
          <span className="inline-flex items-center gap-1">
            <MapPin className="h-3 w-3" /> {thread.location}
          </span>
        )}
        <span>{thread._count.posts} replies</span>
        {typeof thread.price === 'number' && (
          <span className="rounded-full bg-amber-50 px-2 py-0.5 text-amber-600">
            £{thread.price}
          </span>
        )}
      </div>
    </article>
  );
}
