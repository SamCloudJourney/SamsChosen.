import { createServer } from 'http';
import app from './server.js';
import { env } from './config/env.js';
import { logger } from './lib/logger.js';

const server = createServer(app);

server.listen(env.PORT, () => {
  logger.info(`API listening on port ${env.PORT}`);
});
