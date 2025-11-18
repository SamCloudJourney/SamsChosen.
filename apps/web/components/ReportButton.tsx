'use client';

import { Flag } from 'lucide-react';
import { useState } from 'react';
import { apiFetch } from '../lib/api-client';

interface Props {
  threadId?: string;
  postId?: string;
}

export function ReportButton({ threadId, postId }: Props) {
  const [status, setStatus] = useState<'idle' | 'sending' | 'sent'>('idle');

  async function handleReport() {
    setStatus('sending');
    try {
      await apiFetch('/reports', {
        method: 'POST',
        body: {
          reason: 'Flagged from UI',
          threadId,
          postId,
        },
      });
      setStatus('sent');
    } catch (error) {
      setStatus('idle');
      console.error(error);
    }
  }

  return (
    <button
      type="button"
      onClick={handleReport}
      className="inline-flex items-center gap-1 text-xs text-rose-600"
      disabled={status !== 'idle'}
    >
      <Flag className="h-4 w-4" /> {status === 'sent' ? 'Reported' : 'Report'}
    </button>
  );
}
