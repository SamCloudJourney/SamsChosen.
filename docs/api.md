# API Reference

Base URL: `https://{API_HOST}/api`

## Auth
- `POST /auth/register` → `{ user }`
- `POST /auth/login` → `{ user }`
- `POST /auth/refresh` → `{ accessToken, refreshToken }`
- `POST /auth/logout` → `204`

## Users
- `GET /users/:username`
- `PATCH /users/me`

## Categories
- `GET /categories`
- `GET /categories/:slug`

## Threads
- `GET /threads`
- `GET /threads/:id`
- `POST /threads`
- `POST /threads/:id/{pin|unpin|lock|unlock}` (admin)

## Posts
- `POST /posts`

## Notifications
- `GET /notifications?since=`
- `POST /notifications/:id/read`

## Reports & Admin
- `POST /reports`
- `GET /admin/reports`
- `POST /admin/reports/:id`
- `POST /admin/bans`

## Search
- `GET /search?query=keyword&categoryId=&area=`
