"""
Main Application Launcher for JEE Main PYQs Concept Studio.
Starts the FastAPI web server on http://localhost:8000.
"""

import sys
import os
import uvicorn

# Ensure project root is in path
sys.path.insert(0, os.path.abspath('.'))

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

from app.db.database import init_db, DB_PATH


def main():
    print("=" * 60)
    print("      JEE MAIN PYQS CONCEPT STUDIO & REVISION ENGINE        ")
    print("=" * 60)
    
    # Initialize database
    init_db(DB_PATH)
    print(f"[OK] Database initialized at: {DB_PATH}")
    print("[OK] Starting local web dashboard at: http://localhost:8000")
    print("[OK] Open http://localhost:8000 in your browser to start revising!")
    print("=" * 60)

    uvicorn.run(
        "app.web.app:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info"
    )


if __name__ == "__main__":
    main()
