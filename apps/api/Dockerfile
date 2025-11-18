# Build context should be repository root.
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
COPY apps/api/package*.json apps/api/
COPY packages/db/package*.json packages/db/
RUN npm install --workspaces --include-workspace-root=false

FROM node:20-alpine AS builder
WORKDIR /app
COPY . .
RUN npm install --workspaces --include-workspace-root=false --omit=dev
RUN npm run build --workspace=@samchosen/db
RUN npm run build --workspace=apps/api

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/apps/api ./apps/api
WORKDIR /app/apps/api
EXPOSE 4000
CMD ["node", "dist/index.js"]
