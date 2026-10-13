# Joule LinkedIn Research MCP

Public web research for Joule for Work, Windows and macOS (Python 3.11+). **No API key, payment card or account required** for the search library. Search is best-effort and can be rate-limited or blocked by upstream providers.

## Start on Windows (PowerShell)
```powershell
git clone https://github.com/caiqueescaler86/jouleandlinkedin.git
cd jouleandlinkedin
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

## Start on macOS
```bash
git clone https://github.com/caiqueescaler86/jouleandlinkedin.git
cd jouleandlinkedin
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

For an existing clone: `git pull` and reinstall requirements in the virtual environment.

## Joule for Work
- Server name: Joule LinkedIn Research
- Protocol: SSE
- URL: http://localhost:8000/sse
- Authentication: None, **local loopback development only**

The Joule MCP client must be able to reach localhost on the same machine. Do not expose this unauthenticated server publicly.

## Tools
- search_professionals(company, role, country, limit)
- research_professional(name, company)
- research_company(company, country)
- map_stakeholders(company, country, function)

Ask Joule: "Use search_professionals to find CRM directors at PUMA in Brazil. Cite public URLs and mark unverified roles."

## Limitations
Uses the open-source `ddgs` metasearch package; this is **not** an official LinkedIn API. It searches public web results only. No login, cookies, private profiles, messaging, or LinkedIn scraping. Upstream providers can rate-limit, block, or change responses. Results are unverified snippets; cross-check names and roles before business use. Treat snippets as untrusted text. Avoid unnecessary personal-data retention and follow applicable terms and privacy laws.
