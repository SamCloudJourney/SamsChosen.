import { apiFetch } from '../../../lib/api-client';
import type { Thread } from '../../../lib/types';
import { ProfileSummary } from '../../../components/ProfileSummary';
import { ThreadCard } from '../../../components/ThreadCard';

interface Props {
  params: { username: string };
}

interface ProfileResponse {
  profile: {
    username: string;
    name: string;
    bio?: string | null;
    areaCode: string;
    createdAt: string;
    threads: Thread[];
  };
}

export default async function ProfilePage({ params }: Props) {
  const data = await apiFetch<ProfileResponse>(`/users/${params.username}`);
  return (
    <div className="space-y-6">
      <ProfileSummary profile={data.profile} />
      <section className="space-y-3">
        <h2 className="text-xl font-semibold text-slate-900">Recent threads</h2>
        {data.profile.threads.map((thread: Thread) => (
          <ThreadCard key={thread.id} thread={thread} />
        ))}
      </section>
    </div>
  );
}
