#!/bin/bash
set -e
cd "$(dirname "$0")"
echo "Professional Research MCP - macOS setup"
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.11+ is required: https://www.python.org/downloads/"
  echo "Install Python and try again. Git is not required."
  read -r -p "Press Enter to close..."
  exit 1
fi
if ! python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3,11) else 1)'; then
  echo "Python 3.11 or newer is required: https://www.python.org/downloads/"
  read -r -p "Press Enter to close..."
  exit 1
fi
if [ ! -x ".venv/bin/python" ]; then
  echo "Creating Python virtual environment..."
  python3 -m venv .venv
fi
echo "Installing dependencies..."
./.venv/bin/python -m pip install -r requirements.txt
echo
echo "MCP URL: http://127.0.0.1:8000/sse"
echo "Keep this window open while using the MCP client."
echo "Press Ctrl+C to stop the server."
./.venv/bin/python server.py
