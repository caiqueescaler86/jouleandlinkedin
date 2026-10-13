# Professional Research MCP

[English](README.md) | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)

A local MCP server for researching professionals, companies, and potential stakeholders using **publicly indexed web information**. Works with compatible MCP clients supporting local SSE connections.

**Free to install:** no API key, payment card, or LinkedIn account required. Public search providers may rate-limit or block queries.

> **Not an official LinkedIn API or affiliated integration.** No access to private profiles, account connections, messages, or feeds.

## Requirements

- Windows (PowerShell) or macOS (Terminal)
- Python 3.11 or later
- Git
- An MCP client supporting local SSE servers
- Internet connection for public searches

Check your installation:

**Windows**
```powershell
py --version
git --version
```

**macOS**
```bash
python3 --version
git --version
```

Install Python and Git first if needed. On Windows, use `python` instead of `py` if your Python installation does not include the launcher.

## Install on Windows

Open PowerShell and run these commands **one at a time**:

```powershell
git clone https://github.com/caiqueescaler86/jouleandlinkedin.git
cd jouleandlinkedin
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

Leave the terminal open. Expected startup message:

```text
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
```

To start again later, open PowerShell in the project folder and run:

```powershell
.\.venv\Scripts\python.exe server.py
```

## Install on macOS

Open Terminal and run:

```bash
git clone https://github.com/caiqueescaler86/jouleandlinkedin.git
cd jouleandlinkedin
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

Keep Terminal open while using the connector. Restart it later with `./.venv/bin/python server.py`.

## Connect your MCP client

With the Python server running:

1. Open an MCP client that supports local SSE connections.
2. Find its MCP servers / connectors settings (labels vary by client).
3. Add a new MCP server using:

| Setting | Value |
| --- | --- |
| Name | Professional Research |
| URL | `http://127.0.0.1:8000/sse` |
| Transport | SSE |
| Authentication | None (local development only) |

4. Save and enable the connection.
5. Verify that the four tools appear in your MCP client.

**Use `127.0.0.1` instead of `localhost`:**

```text
http://127.0.0.1:8000/sse
```

The MCP client must run on the same computer or have explicit access to its loopback server. A cloud-only client cannot automatically access your computer's `127.0.0.1`.

## Try it

Ask your MCP client:

```text
Use research_professional to find public professional references
for "Example Person". Include source URLs and do not invent facts.
```

```text
Use map_stakeholders to identify potential marketing and CRM
stakeholders at Example Company in Brazil. Cite sources and
flag unverified job titles or decision-making authority.
```

## Available tools

| Tool | Purpose |
| --- | --- |
| `search_professionals(company, role, country, limit)` | Find publicly indexed professionals by company, role and country |
| `research_professional(name, company)` | Research public references to a person |
| `research_company(company, country)` | Find public company information |
| `map_stakeholders(company, country, function)` | Discover possible stakeholders |

Results are **unverified research leads**, not confirmed identities, employment or decision-making authority.

## Troubleshooting

**Cannot connect:** Confirm that the Python server is running and the URL is exactly `http://127.0.0.1:8000/sse`. If you previously used `localhost`, recreate the connection with `127.0.0.1`.

**Check SSE on Windows** (in a second PowerShell window):

```powershell
curl.exe -N --max-time 5 http://127.0.0.1:8000/sse
```

Expected beginning:

```text
event: endpoint
data: /messages/?session_id=...
```

The five-second timeout is normal for a persistent SSE connection. This checks the SSE endpoint, **not** the full MCP tool handshake.

**Repeated `GET /sse 200 OK`:** The client may be reconnecting. HTTP 200 alone does not prove successful MCP initialization.

**`MCP error -32602: Invalid request parameters`:** Reconnect the client. If it persists, collect the exact error and server logs to investigate request compatibility.

**`Error: name 'clean' is not defined`:** Update the repository; this bug was fixed. Restart the server.

**No search results:** Public search providers may be unavailable or rate-limited. Empty results do not necessarily mean the MCP connection failed.

## Update

Stop the server with `Ctrl+C`, then run:

**Windows**
```powershell
git pull
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

**macOS**
```bash
git pull
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

## Security and limitations

- The server binds to `127.0.0.1` by default. **Never expose it publicly without authentication.**
- Searches use the `ddgs` public metasearch package, not authenticated LinkedIn access.
- Verify sources and professional details before making business decisions.
- Follow provider terms, corporate policies, and applicable privacy laws.
