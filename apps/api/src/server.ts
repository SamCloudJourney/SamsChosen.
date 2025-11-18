import compression from 'compression';
import cookieParser from 'cookie-parser';
import cors from 'cors';
import express from 'express';
import helmet from 'helmet';
import morgan from 'morgan';
import createError from 'http-errors';
import { env } from './config/env.js';
import { requestLogger } from './middleware/request-logger.js';
import { errorHandler } from './middleware/error-handler.js';
import routes from './routes/index.js';

const app = express();

app.use(helmet());
app.use(compression());
app.use(
  cors({
    origin: env.CORS_ORIGIN.split(','),
    credentials: true,
  })
);
app.use(express.json({ limit: '1mb' }));
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(morgan('combined'));
app.use(requestLogger);

app.use('/api', routes);

app.use((req, res, next) => {
  next(createError(404, 'Route not found'));
});

app.use(errorHandler);

export default app;
