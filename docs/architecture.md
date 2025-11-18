# Architecture Overview

## System Diagram
```
[Next.js 14 Frontend] --HTTPS--> [Express API] --Prisma--> [PostgreSQL]
                                     |
                                [Sentry]
                                     |
                                [Logging]
```

## Key Design Decisions
- **Lean monorepo** keeps focus on two deployables (`apps/web`, `apps/api`) and a shared Prisma package (`packages/db`).
- **Polling notifications** every 15s deliver timely updates without maintaining WebSockets in v1.
- **Security-first auth** uses Argon2, rotating refresh tokens, and HttpOnly cookies.
- **Moderation hooks** (reports, bans, locks, pins) exist from day one to keep the community healthy.

## Deployment Targets
- Frontend → Vercel (App Router, standalone output).
- Backend → Any Node-friendly host or container platform (Render, Fly.io). Dockerfile lives under `apps/api`.
- Database → Managed PostgreSQL (Supabase, Neon, RDS). Backups + migrations handled through Prisma.

## Observability & Safety
- Structured logging via Pino.
- Optional Sentry DSNs for both web and API (surfaced in env examples + README).
- Rate limiting, CAPTCHA stubs, mention filtering, and admin bans reduce spam/abuse vectors.
