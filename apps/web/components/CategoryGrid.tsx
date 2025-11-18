import Link from 'next/link';
import type { Category } from '../lib/types';

interface Props {
  categories: Category[];
}

export function CategoryGrid({ categories }: Props) {
  return (
    <div className="grid gap-4 md:grid-cols-2">
      {categories.map((category) => (
        <Link
          key={category.id}
          href={`/categories/${category.slug}`}
          className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition hover:-translate-y-0.5"
        >
          <p className="text-xs font-semibold uppercase tracking-widest text-brand-500">
            {category.slug.replace('-', ' ')}
          </p>
          <h3 className="mt-1 text-lg font-semibold text-slate-900">{category.name}</h3>
          <p className="text-sm text-slate-600">{category.description}</p>
        </Link>
      ))}
    </div>
  );
}
