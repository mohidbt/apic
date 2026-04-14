# Contributing to API Ingest

Thanks for your interest in contributing.

## Development Setup

1. Clone the repository.
2. Start the backend:
   - `cd backend`
   - `python3 -m venv venv && source venv/bin/activate`
   - `pip install -r requirements.txt`
   - `python main.py`
3. Start the frontend in a second terminal:
   - `cd frontend`
   - `npm install`
   - `echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local`
   - `npm run dev`

## Before Opening a PR

- Backend tests: `cd backend && pytest tests/ -v`
- Frontend checks: `cd frontend && npm run lint && npm run test`
- Keep changes focused and include docs updates when behavior changes.

## Pull Request Guidelines

- Use clear commit messages describing intent.
- Link related issues in the PR description.
- Include a short test plan and results.
- Add screenshots for UI changes.

## Reporting Bugs

Open a GitHub issue and include:

- Steps to reproduce
- Expected behavior
- Actual behavior
- Logs/error output (sanitized)
- Example spec file if relevant
