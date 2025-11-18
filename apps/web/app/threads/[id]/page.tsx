import { apiFetch } from '../../../lib/api-client';
import type { Post, Thread } from '../../../lib/types';
import { AreaBadge } from '../../../components/AreaBadge';
import { ReportButton } from '../../../components/ReportButton';

interface Props {
  params: { id: string };
}

export default async function ThreadPage({ params }: Props) {
  const data = await apiFetch<{ thread: Thread & { posts: Post[] } }>(`/threads/${params.id}`);
  const thread = data.thread;
  return (
    <article className="space-y-6">
      <header className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
        <div className="flex items-start justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Thread</p>
            <h1 className="text-3xl font-semibold text-slate-900">{thread.title}</h1>
            <p className="mt-2 text-sm text-slate-600">{thread.content}</p>
          </div>
          <AreaBadge area={thread.author.areaCode} />
        </div>
        <div className="mt-4 flex items-center justify-between text-xs text-slate-500">
          <span>by @{thread.author.username}</span>
          <ReportButton threadId={thread.id} />
        </div>
      </header>
      <section className="space-y-3">
        {thread.posts.map((post) => (
          <div key={post.id} className="rounded-2xl border border-slate-200 bg-white p-4">
            <div className="flex items-center justify-between">
              <p className="text-sm font-semibold text-slate-900">@{post.author.username}</p>
              <AreaBadge area={post.author.areaCode} />
            </div>
            <p className="mt-2 text-sm text-slate-700">{post.content}</p>
            <div className="mt-2 text-xs text-slate-500">
              {new Date(post.createdAt).toLocaleString('en-GB')}
            </div>
            <div className="mt-2">
              <ReportButton postId={post.id} />
            </div>
          </div>
        ))}
      </section>
    </article>
  );
}
