# Bloknot

Bloknot front-end: https://github.com/datogoglidze/bloknot-front.git

A simple note-taking API, where you can create and list notes

## Quick start
* Run (dev):
  * Create `.env` file in `bloknot` folder;
  * Insert SQLite database location: `DSN = "bloknot.sqlite"` and front-end url (if using bloknot-front `npm run dev`): `FRONTEND_URL = "http://localhost:5173"`;
  * Run `make run` and access it on: `http://localhost:8000`.
####
* Run (prod):
  * Pull Docker image: `ghcr.io/datogoglidze/bloknot:latest`;
  * Run it as a container:
    * With port: `port_you_want:8000`;
    * Environment variables:
      * `TZ: "your_timezone"`;
      * `DSN: "/var/databases/bloknot.sqlite"`;
      * `FRONTEND_URL: "http://example_url"` (if using bloknot-front).
    * Create Docker volume for SQLite persistence: `bloknot-databases:/var/databases`.
  * And access it on `http://docker_url:port_you_want` (locally it's: `http://localhost:port_you_want`).
