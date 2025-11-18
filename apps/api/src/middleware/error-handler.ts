import type { NextFunction, Request, Response } from 'express';
import { logger } from '../lib/logger.js';
import { reportError } from '../lib/telemetry.js';

export function errorHandler(
  err: Error & { status?: number },
  _req: Request,
  res: Response,
  _next: NextFunction
) {
  const statusCode = err.status || 500;
  logger.error({ err }, 'request failed');
  reportError(err).catch(() => undefined);
  res.status(statusCode).json({
    error: {
      message: err.message || 'Internal server error',
    },
  });
}
