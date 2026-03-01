# Wallet Management System

A full-stack Wallet Management System with a Node.js/Express backend and a React + Tailwind frontend. This repository contains the backend API and the frontend client used to manage users, wallets, transactions, and referrals.

## Features

- User registration and authentication (JWT)
- Wallet creation and balance management
- Transaction recording and listing
- Referral tracking
- Clean separation of backend API and frontend client

## Tech Stack

- Backend: Node.js, Express, MongoDB (Mongoose)
- Frontend: React, Vite / Create React App (depending on setup), Tailwind CSS
- Auth: JWT

## Repository Structure

- `backend/` — Express API, controllers, models, routes
- `frontend/` — React application, components, styles

## Prerequisites

- Node.js (v16+ recommended)
- npm or yarn
- MongoDB (local or hosted, e.g., MongoDB Atlas)

## Environment Variables

Create an `.env` file in the `backend/` folder with the following variables (example names):

- `PORT` — Port for the backend server (e.g. `5000`)
- `MONGO_URI` — MongoDB connection string
- `JWT_SECRET` — Secret key for signing JWTs
- `CLIENT_URL` — (optional) Frontend origin for CORS

In the `frontend/` project, set the API base URL (example using CRA or Vite env naming):

- `REACT_APP_API_URL` (or `VITE_API_URL`) — e.g. `http://localhost:5000/api`

## Setup & Run

Backend

1. Change to the backend directory and install dependencies:

```bash
cd backend
npm install
```

2. Create the `.env` file (see Environment Variables above).

3. Start the backend in development mode:

```bash
npm run dev
# or
node server.js
```

Frontend

1. Change to the frontend directory and install dependencies:

```bash
cd frontend
npm install
```

2. Create/adjust environment variables (set `REACT_APP_API_URL` or `VITE_API_URL`).

3. Start the frontend in development mode:

```bash
npm start
# or (if using Vite)
npm run dev
```

## API Endpoints (Overview)

This project exposes the API under a base path like `/api`. See the `backend/routes` folder for exact routes and handlers. Common routes include:

- `POST /api/auth/register` — register a new user
- `POST /api/auth/login` — log in and receive a JWT
- `GET /api/wallet` — get authenticated user's wallet/balance
- `POST /api/wallet/transactions` — create a transaction (deposit/withdraw/transfer)
- `GET /api/transactions` — list user's transactions
- `POST /api/referrals` — create or apply a referral
- `GET /api/referrals` — list referrals

Protect routes using the JWT authentication middleware located in `backend/middleware/auth.js`.

## Database

The backend uses MongoDB via Mongoose models in `backend/models/`. Start a local MongoDB service or provide a hosted connection via `MONGO_URI`.

## Development Notes

- Controllers are in `backend/controllers/` and map to routes in `backend/routes/`.
- Models live in `backend/models/`.
- Frontend React components are in `frontend/src/components/`.
- Use Postman / Insomnia to test API endpoints; include the `Authorization: Bearer <token>` header for protected endpoints.

## Testing

This repository does not include automated tests by default. To add tests, consider Jest for the backend and React Testing Library for the frontend.

## Contributing

Contributions are welcome. Typical workflow:

1. Fork the repo
2. Create a feature branch
3. Make changes and add tests
4. Submit a pull request with a clear description

## License

Specify your license here (e.g., MIT) or add a `LICENSE` file in the repo.

## Where to look next

- `backend/server.js` — backend entry point
- `backend/routes/` — endpoint definitions
- `frontend/src/` — React app entry and components

If you'd like, I can:

- add a README badge and quick screenshots
- create a `CONTRIBUTING.md` or `LICENSE`
- open a PR with these changes

---

File: [README.md](README.md)
