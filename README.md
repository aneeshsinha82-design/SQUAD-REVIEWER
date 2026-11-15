# FC Mobile Squad Finder

A Windows-friendly local website prototype for searching FC Mobile squads by UID.

## Run on Windows
1. Install Python 3 from https://www.python.org/downloads/ (enable **Add Python to PATH**).
2. Download or clone this repository.
3. Double-click **START.bat**.
4. Open http://localhost:8000 in Chrome or Edge.

## Current implementation status
- Responsive UID search interface.
- Squad summary and formation-pitch display.
- Local Python HTTP server and API route at /api/squad.
- Live lookup is intentionally not faked: the API route returns HTTP 501 until a verified FC Mobile UID-to-squad provider is identified and integrated.

## API and security
EA's FC Community API is restricted to approved partners and is not a general public arbitrary-UID lookup service. Reverse-engineered endpoints must be verified specifically against FC Mobile before use. Never request or store EA passwords, session cookies, or authentication tokens from users.

This is an independent fan project and is not affiliated with Electronic Arts.
