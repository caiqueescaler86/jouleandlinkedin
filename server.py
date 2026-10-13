"""Read-only public professional research MCP for Joule for Work."""
import os
import re
from datetime import datetime, timezone
from urllib.parse import urlparse

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()
mcp = FastMCP("Joule LinkedIn Research", host=os.getenv("MCP_HOST", "127.0.0.1"), port=int(os.getenv("MCP_PORT", "8000")))
def clean(value: str, maximum: int = 140) -> str:
    """Validate user-supplied search terms before building a query."""
    value = re.sub(r"[\r\n\t]+", " ", value or "").strip()
    if not value or len(value) > maximum:
        raise ValueError("Provide a non-empty search term within the length limit")
    return value


async def search(query: str, count: int = 8) -> dict:
    """Best-effort public metasearch; no account or API key required."""
    from ddgs import DDGS
    try:
        # ddgs is synchronous: run it outside the async event loop.
        import asyncio
        raw = await asyncio.to_thread(
            lambda: list(DDGS(timeout=15).text(query, max_results=max(1, min(count, 10))))
        )
    except Exception as exc:
        return {"error": f"Public search unavailable: {type(exc).__name__}",
                "results": [], "query": query}
    results = []
    seen = set()
    for item in raw:
        url = item.get("href") or item.get("url") or ""
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc or url in seen:
            continue
        seen.add(url)
        results.append({
            "title": item.get("title", ""),
            "url": url,
            "snippet": item.get("body") or item.get("description", ""),
            "source_domain": parsed.netloc.lower(),
        })
    return {"query": query, "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "results": results,
            "notice": "Search snippets are unverified. Search availability and rate limits vary; do not claim verified employment or identity."}


@mcp.tool()
async def search_professionals(company: str, role: str, country: str = "", limit: int = 8) -> dict:
    """Find publicly indexed professional pages by company, role and optional country; results are leads, not verified identities."""
    q = f'site:linkedin.com/in/ "{clean(company)}" "{clean(role)}"'
    if country.strip():
        q += f' "{clean(country)}"'
    return await search(q, limit)


@mcp.tool()
async def research_professional(name: str, company: str = "") -> dict:
    """Find public references for a named professional. Does not access private LinkedIn profile data."""
    q = f'"{clean(name)}"'
    if company.strip():
        q += f' "{clean(company)}"'
    return await search(q + " LinkedIn career biography", 8)


@mcp.tool()
async def research_company(company: str, country: str = "") -> dict:
    """Find official company information, leadership and recent public coverage."""
    q = f'"{clean(company)}"'
    if country.strip():
        q += f' "{clean(country)}"'
    return await search(q + " official website leadership marketing news", 10)


@mcp.tool()
async def map_stakeholders(company: str, country: str = "", function: str = "marketing CRM") -> dict:
    """Discover possible decision-makers through public results; does not infer authority as fact."""
    q = f'"{clean(company)}" "{clean(function)}" (director OR head OR VP OR chief)'
    if country.strip():
        q += f' "{clean(country)}"'
    result = await search(q, 10)
    result["guidance"] = "Return candidates with citations, mark titles and decision authority unverified until independently corroborated."
    return result


if __name__ == "__main__":
    # Legacy SSE endpoint /sse matching the Joule for Work screenshot.
    mcp.run(transport="sse")
