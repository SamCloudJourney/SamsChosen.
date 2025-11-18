import { SearchForm } from '../../components/SearchForm';

export default function SearchPage() {
  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-2xl font-semibold text-slate-900">Search the Forum</h1>
        <p className="text-sm text-slate-600">Find threads by keyword, category, or area.</p>
      </div>
      <SearchForm />
    </div>
  );
}
