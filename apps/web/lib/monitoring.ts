'use client';

const sentryDsn = process.env.NEXT_PUBLIC_SENTRY_DSN;

export function logClientError(error: Error) {
  console.error(error);
  if (!sentryDsn) {
    return;
  }
  try {
    const payload = {
      message: error.message,
      stack: error.stack,
      timestamp: new Date().toISOString(),
    };
    navigator.sendBeacon?.(sentryDsn, JSON.stringify(payload));
  } catch (sendError) {
    console.error('Failed to report error', sendError);
  }
}
