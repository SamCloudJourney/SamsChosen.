'use client';

import { useState } from 'react';
import { apiFetch } from '../lib/api-client';
import { logClientError } from '../lib/monitoring';

interface Props {
  mode: 'login' | 'register';
}

export function AuthForm({ mode }: Props) {
  const [formState, setFormState] = useState({
    email: '',
    password: '',
    username: '',
    name: '',
    areaCode: 'SE22',
  });
  const [error, setError] = useState<string | null>(null);
  const [status, setStatus] = useState<'idle' | 'submitting' | 'success'>('idle');

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    setStatus('submitting');
    setError(null);
    try {
      const body =
        mode === 'login'
          ? { email: formState.email, password: formState.password }
          : formState;
      await apiFetch(`/auth/${mode === 'login' ? 'login' : 'register'}`, {
        method: 'POST',
        body,
      });
      setStatus('success');
    } catch (err) {
      setStatus('idle');
      setError(err instanceof Error ? err.message : 'Failed to authenticate');
      if (err instanceof Error) {
        logClientError(err);
      }
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {mode === 'register' && (
        <>
          <input
            className="w-full rounded-xl border border-slate-200 px-3 py-2"
            placeholder="Name"
            value={formState.name}
            onChange={(event) => setFormState({ ...formState, name: event.target.value })}
          />
          <input
            className="w-full rounded-xl border border-slate-200 px-3 py-2"
            placeholder="Username"
            value={formState.username}
            onChange={(event) => setFormState({ ...formState, username: event.target.value })}
          />
          <select
            className="w-full rounded-xl border border-slate-200 px-3 py-2"
            value={formState.areaCode}
            onChange={(event) => setFormState({ ...formState, areaCode: event.target.value })}
          >
            <option value="SE22">SE22</option>
            <option value="SE15">SE15</option>
          </select>
        </>
      )}
      <input
        className="w-full rounded-xl border border-slate-200 px-3 py-2"
        placeholder="Email"
        type="email"
        value={formState.email}
        onChange={(event) => setFormState({ ...formState, email: event.target.value })}
      />
      <input
        className="w-full rounded-xl border border-slate-200 px-3 py-2"
        placeholder="Password"
        type="password"
        value={formState.password}
        onChange={(event) => setFormState({ ...formState, password: event.target.value })}
      />
      {error && <p className="text-sm text-rose-600">{error}</p>}
      <button
        className="w-full rounded-full bg-brand-600 py-2 text-white"
        disabled={status === 'submitting'}
      >
        {status === 'submitting' ? 'Please wait…' : mode === 'login' ? 'Sign in' : 'Create account'}
      </button>
      {status === 'success' && <p className="text-sm text-emerald-600">Success! Refresh to continue.</p>}
    </form>
  );
}
