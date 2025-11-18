import { env } from '../config/env.js';
import { logger } from './logger.js';

export async function reportError(error: Error) {
  if (!env.SENTRY_DSN) {
    return;
  }
  try {
    await fetch(env.SENTRY_DSN, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: error.message,
        stack: error.stack,
        timestamp: new Date().toISOString(),
      }),
    });
  } catch (telemetryError) {
    logger.warn({ telemetryError }, 'Failed to report error');
  }
}
