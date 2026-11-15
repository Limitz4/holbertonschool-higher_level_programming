# RESTful API Development with Python

## Overview

This project explores HTTP APIs from both the client and server perspectives. It progresses from consuming a public API to building simple Python HTTP services, creating Flask endpoints, and demonstrating authentication and role-based access control.

## Project Files

| File | Description |
| --- | --- |
| `task_02_requests.py` | Fetches JSONPlaceholder posts with `requests`, prints titles, and exports selected fields to a CSV file. |
| `main_02_requests.py` | Small entry point for the API-client exercise. |
| `task_03_http_server.py` | Implements a minimal HTTP GET API with Python's `http.server`. |
| `task_04_flask.py` | Implements Flask routes for viewing and adding user data. |
| `task_05_basic_security.py` | Demonstrates HTTP Basic Authentication, JWT-protected routes, and an admin-only endpoint. |

## Example Endpoints

### Flask user API (`task_04_flask.py`)

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/` | Welcome message |
| `GET` | `/status` | Basic status response |
| `GET` | `/data` | List known user names |
| `GET` | `/users/<username>` | Look up one user |
| `POST` | `/add_user` | Create a user from JSON data |

### Authentication demo (`task_05_basic_security.py`)

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/basic-protected` | Requires HTTP Basic Authentication |
| `POST` | `/login` | Validates credentials and issues a JWT |
| `GET` | `/jwt-protected` | Requires a valid JWT |
| `GET` | `/admin-only` | Requires an admin role in JWT claims |

## Local Setup

Install the packages needed by the different exercises:

```bash
python3 -m pip install requests flask flask-httpauth flask-jwt-extended
```

Run the Flask user API:

```bash
python3 task_04_flask.py
```

In another terminal:

```bash
curl http://127.0.0.1:5000/status
curl http://127.0.0.1:5000/data
```

Start the separate authentication demo with:

```bash
python3 task_05_basic_security.py
```

## Skills Practiced

- Consuming HTTP APIs and parsing JSON responses.
- Exporting fetched data to CSV.
- Implementing GET and POST endpoints in Python.
- Returning appropriate HTTP status codes and JSON errors.
- Understanding credential verification, password hashing, JWTs, and role checks.

## Security Notice

The authentication example contains **hard-coded demonstration credentials and signing keys** and runs Flask with `debug=True`. It is intended only for local learning. It must not be exposed to an untrusted network or used as a production authentication service. A production design would load secrets securely, disable debug mode, enforce HTTPS, use persistent storage, and add appropriate rate limiting and operational controls.

