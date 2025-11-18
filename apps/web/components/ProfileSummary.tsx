import { AreaBadge } from './AreaBadge';

interface Props {
  profile: {
    username: string;
    name: string;
    bio?: string | null;
    areaCode: string;
    createdAt: string;
  };
}

export function ProfileSummary({ profile }: Props) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm text-slate-500">@{profile.username}</p>
          <h1 className="text-2xl font-semibold text-slate-900">{profile.name}</h1>
          {profile.bio && <p className="mt-2 text-sm text-slate-600">{profile.bio}</p>}
        </div>
        <AreaBadge area={profile.areaCode} />
      </div>
      <p className="mt-4 text-xs text-slate-500">
        Member since {new Date(profile.createdAt).toLocaleDateString('en-GB')}
      </p>
    </div>
  );
}
