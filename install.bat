@echo off
setlocal
cd /d "%~dp0"
echo Professional Research MCP - Windows setup
where py >nul 2>&1
if %errorlevel%==0 (
  set "PYTHON=py -3"
) else (
  where python >nul 2>&1
  if errorlevel 1 goto missing
  set "PYTHON=python"
)
if not exist ".venv\Scripts\python.exe" (
  echo Creating Python virtual environment...
  %PYTHON% -m venv .venv
  if errorlevel 1 goto failure
)
echo Installing dependencies...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failure
echo.
echo MCP URL: http://127.0.0.1:8000/sse
echo Keep this window open while using the MCP client.
echo Press Ctrl+C to stop the server.
".venv\Scripts\python.exe" server.py
if errorlevel 1 goto failure
goto done
:missing
echo Python 3.11 or newer is required.
echo Download it from https://www.python.org/downloads/
echo Then run this file again. Git is not required.
goto failure
:failure
echo.
echo Setup or server failed. Review the message above.
pause
exit /b 1
:done
endlocal
