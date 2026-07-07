import os
import sys
import time
import webbrowser
import subprocess

# Get application folder
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

backend = os.path.join(BASE_DIR, "backend")
frontend = os.path.join(BASE_DIR, "frontend", "index.html")

# Check folders
if not os.path.exists(backend):
    raise Exception(f"Backend folder not found:\n{backend}")

if not os.path.exists(frontend):
    raise Exception(f"Frontend not found:\n{frontend}")

# Start backend
server = subprocess.Popen(
    ["python", "server.py"],
    cwd=backend
)

# Wait for server
time.sleep(3)

# Open browser
webbrowser.open(frontend)

server.wait()