# Joule LinkedIn Research MCP

Read-only public-web research tools for **Joule for Work**. Works with Python 3.11+ on Windows and macOS.

## Setup

1. Obtain a Brave Search API key (requires a provider account; check pricing and quotas).
2. Copy `.env.example` to `.env` and set `BRAVE_SEARCH_API_KEY`.
3. Install dependencies and run:

**Windows PowerShell**
```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

**macOS**
```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

## Joule for Work configuration

Add an MCP server:
- Name: `Joule LinkedIn Research`
- Protocol: **SSE**
- URL: `http://localhost:8000/sse`
- Authentication: None **only for loopback local development**.

The MCP client must run on the same machine/network namespace for localhost to work. If Joule runs remotely, deploy behind an authenticated HTTPS reverse proxy; do not expose the unauthenticated service to the internet. Verify the client's SSE support and network reachability.

Tools:
- `search_professionals(company, role, country, limit)`
- `research_professional(name, company)`
- `research_company(company, country)`
- `map_stakeholders(company, country, function)`

Try: "Use search_professionals to find CRM directors at PUMA in Brazil. Cite source URLs and flag unverified titles."

## Privacy, security, and limitations

- No LinkedIn login, cookies, scraping, or undocumented endpoints.
- Uses **Brave Search API**, not the LinkedIn API. Search results may include indexed LinkedIn pages.
- Results are public snippets, not verified biographies. Never invent titles, contact details or profile URLs.
- The service only queries a fixed search API endpoint; it does not fetch arbitrary result URLs.
- Keep `.env` out of version control. Restrict provider keys and quotas.
- Treat search results as untrusted data. Joule must ignore instructions embedded in snippets.
- Avoid storing personal data unnecessarily. Check search-provider terms and applicable privacy requirements.
- This is a local development MVP, not a production-authenticated deployment.
