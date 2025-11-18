# Operational Playbook

## Local Development
1. Install dependencies: `npm install` (from repo root).
2. Duplicate env files (`apps/web/.env.example`, `apps/api/.env.example`).
3. Start Postgres (Docker compose snippet in README) and run `npm run prisma:migrate --workspace=@samchosen/db` once.
4. Run both apps concurrently: `npm run dev` → Turbo spawns `next dev` + `ts-node-dev`.

## Deployment
- **Web**: `npm run build --workspace=web`, deploy `.next/standalone` to Vercel. Environment variables live in Vercel dashboard.
- **API**: Build container via `docker build -f apps/api/Dockerfile .` (root context). Push to Fly.io/Render/Heroku. Provide `DATABASE_URL`, `JWT_SECRET`, etc.
- **Database**: Use managed Postgres with daily automated backups. Run `npx prisma migrate deploy` during backend deploy.

## Observability
- Set `SENTRY_DSN` (API) and `NEXT_PUBLIC_SENTRY_DSN` (web) to surface runtime errors.
- Logs: Pino structured logs shipped to stdout; configure host to collect.

## Security & Moderation
- Rate limiter + Argon2 + refresh token rotation already wired.
- Add CAPTCHA service keys before going public to slow bots.
- Admin tools: bans, thread locks, pin/unpin, report triage endpoints.
