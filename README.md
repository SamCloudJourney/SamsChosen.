# East Dulwich Forum — `samchosen`

A modern, hyper-local forum for SE22 + SE15 inspired by the classic East Dulwich Forum. Residents can register, browse categories, start threads, reply, report content, search discussions, and manage notifications. Admins can pin/lock threads, ban users, and triage reports.

## Product Vision
- **Hyper-local identity:** Every surface celebrates SE22/SE15 (area badges, language, imagery).
- **Safe conversations:** Moderation tooling (reports, bans, locks) + rate limits guard the community.
- **Sustainable v1:** Polling notifications, lean monorepo, and pragmatic test suite keep iteration fast while leaving room for Phase 2 (WebSockets, queues, Playwright).

## Repository Layout
```
apps/
  web/     → Next.js 14 App Router frontend (Vercel-ready)
  api/     → Express + Prisma API server (container-ready)
packages/
  db/      → Prisma schema, migrations, seed helpers
scripts/   → Dev/ops helpers (placeholder for future automation)
docs/      → Architecture, API, and ops notes
```

## Key Features
- Auth (register, login, refresh, logout) with Argon2 hashing + HttpOnly cookies.
- Categories + threads + replies with mentions and price/location metadata.
- Search across threads with category/area filters.
- Notifications fetched every 15 seconds (phase 2: upgrade to WebSockets).
- Moderation: report posts/threads, admin review queue, bans, locks, pins.
- Local identity UI components (area badges, SE22/SE15 copy).
- Observability hooks (Pino logs, optional Sentry DSNs) + rate limiting, mention sanitisation, CAPTCHA stub.

## Getting Started
1. **Install dependencies**
   ```bash
   npm install
   ```
2. **Environment variables**
   - Copy `apps/web/.env.example` → `apps/web/.env.local` and set `NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_SENTRY_DSN` (optional).
   - Copy `apps/api/.env.example` → `apps/api/.env` and set:
     - `DATABASE_URL`
     - `JWT_SECRET` (32+ chars)
     - `JWT_REFRESH_SECRET`
     - `COOKIE_DOMAIN`
    - `CORS_ORIGIN` (comma-separated origins)
    - `SENTRY_DSN` (optional)
    - `CAPTCHA_SECRET` (optional shared secret for the simple signup/post challenge)
3. **Database**
   - Start PostgreSQL locally (example Docker compose):
     ```yaml
     services:
       db:
         image: postgres:15
         environment:
           POSTGRES_USER: samchosen
           POSTGRES_PASSWORD: password
           POSTGRES_DB: samchosen
         ports:
           - "5432:5432"
     ```
   - Apply migrations + seed base data:
     ```bash
     cd packages/db
     npx prisma migrate dev
     npx ts-node src/seed.ts
     ```
4. **Run everything**
   ```bash
   npm run dev
   ```
   Turbo starts `next dev` (port 3000) and `ts-node-dev` API (port 4000). The frontend proxies to the API via `NEXT_PUBLIC_API_URL`.

## Testing & Quality Gates
- Lint all workspaces: `npm run lint`
- Run Jest suites (API + Web): `npm run test`
- Formatting: `npm run format`

## Security & Moderation Controls
- Argon2id password hashing and JWT rotation with refresh token blacklist.
- Rate limiter middleware + brute-force protection on auth.
- Input validation via Zod (backend + frontend forms) and sanitized mentions.
- Admin-only APIs for report triage, user bans, and thread locks/pins.
- Simple CAPTCHA header (`X-Captcha-Answer`) gate for registrations/posts when `CAPTCHA_SECRET` is configured.
- When enabled, backend expects `X-Captcha-Answer: <CAPTCHA_SECRET>` on thread/post creation and registration requests (swap with your challenge verifier once ready).
- Logging + optional Sentry DSNs to monitor suspicious behaviour.

## Deployment
### Frontend (Vercel)
1. Create a new Vercel project pointing to `apps/web`.
2. Build command: `npm run build --workspace=web`
3. Install command: `npm install`
4. Output directory: `.next`
5. Environment variables:
   - `NEXT_PUBLIC_API_URL=https://api.yourdomain.com/api`
   - `NEXT_PUBLIC_SENTRY_DSN` (optional)
6. After deploy, configure domain + preview protection.

### Backend (Container host e.g., Fly.io/Render)
1. Ensure build context is repo root and run:
   ```bash
   docker build -f apps/api/Dockerfile -t east-dulwich-api .
   docker run -p 4000:4000 --env-file apps/api/.env east-dulwich-api
   ```
2. Provision managed PostgreSQL + run `npx prisma migrate deploy` inside the container or CI before release.
3. Set environment variables per `.env.example` plus:
   - `NODE_ENV=production`
   - `SENTRY_DSN` (optional)
4. Configure HTTPS + WAF/rate limiting at the edge (Cloudflare, Fly proxy, etc.).

### Database Migrations & Backups
- All schema definitions live in `packages/db/prisma/schema.prisma`.
- Use `npx prisma migrate dev` (local) / `npx prisma migrate deploy` (prod) before releasing.
- Schedule automatic backups via your managed Postgres provider (daily snapshot recommended) and test restore quarterly.

## Phase 2 Hooks
- Socket.IO + Bull queue stubs for real-time notifications/job processing.
- Shared UI package + design tokens once the design stabilises.
- Playwright end-to-end suite after product requirements settle.

## Maintenance Tips
- Track moderation actions with exported Pino logs + Sentry breadcrumbs.
- Run `packages/db/src/seed.ts` anytime you need baseline categories or a default admin (requires pre-hashed password envs).
- Update `docs/` whenever contracts or architecture change.

## Deployment Checklist
- [ ] `npm test` and `npm run lint`
- [ ] `npx prisma migrate deploy` against production DB
- [ ] Docker image built from root context
- [ ] Vercel envs updated with latest API host
- [ ] Backups confirmed (DB + .env) prior to cutover
