import { AuthForm } from '../../../components/AuthForm';

export default function LoginPage() {
  return (
    <div className="mx-auto max-w-md space-y-4 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <h1 className="text-2xl font-semibold text-slate-900">Welcome back</h1>
      <AuthForm mode="login" />
    </div>
  );
}
