# Python Network Programming: HTTP Requests and APIs

## Overview

This project demonstrates how Python programs interact with HTTP services. The exercises use both the Python standard library (`urllib`) and the third-party `requests` package to retrieve response bodies, read HTTP headers, send POST requests, handle HTTP errors, and parse JSON API responses.

## Exercises

| File | Main Focus |
| --- | --- |
| `0-hbtn_status.py` | Fetch an HTTP response using `urllib` and inspect its bytes and decoded text. |
| `1-hbtn_header.py` | Read the `X-Request-Id` response header with `urllib`. |
| `2-post_email.py` | Submit form data through an HTTP POST request using `urllib`. |
| `3-error_code.py` | Catch HTTP errors and print their status codes. |
| `4-hbtn_status.py` | Fetch an HTTP response using `requests`. |
| `5-hbtn_header.py` | Read an HTTP response header using `requests`. |
| `6-post_email.py` | Submit form data with `requests.post`. |
| `7-error_code.py` | Work with non-success HTTP status codes. |
| `8-json_api.py` | Query an API endpoint and parse its JSON response. |
| `10-my_github.py` | Demonstrate a user-account API request to GitHub. |
| `100-github_commits.py` | Fetch and display recent commit information from the GitHub API. |

## Tools and Concepts

- Python 3
- `urllib.request`, `urllib.error`, and `requests`
- HTTP GET and POST methods
- Response headers and status codes
- URL-encoded form data and JSON
- Basic API integration and response parsing

## Getting Started

Install the package used by the `requests` exercises:

```bash
python3 -m pip install requests
```

One example that can be adapted to a public GitHub repository:

```bash
python3 100-github_commits.py holbertonschool-network Limitz4
```

This calls GitHub's public commits endpoint and prints commit SHAs and author names. API responses depend on network access and rate limits.

## Skills Demonstrated

- Sending and inspecting HTTP requests in Python.
- Handling server responses and error codes.
- Processing JSON data from APIs.
- Working with an external REST API to retrieve repository metadata.

## Compatibility and Security Notes

- Several exercises reference school-hosted endpoints or local practice servers that may not be available outside the original lab environment.
- `10-my_github.py` demonstrates **legacy username/password HTTP authentication**. GitHub no longer supports password-based API authentication for normal use. Do not enter your GitHub password into this script; use a properly scoped token or supported authentication method when building new integrations.
- Never commit API tokens or private credentials to source control.

