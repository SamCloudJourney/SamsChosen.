'use client';

interface Props {
  area: string;
}

export function AreaBadge({ area }: Props) {
  return (
    <span className="inline-flex items-center rounded-full bg-brand-50 px-2 py-0.5 text-xs font-semibold text-brand-600">
      {area}
    </span>
  );
}
