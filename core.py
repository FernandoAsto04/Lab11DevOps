from datetime import datetime, timezone

def payload():
    return {
        "ok": True,
        "ts": datetime.now(timezone.utc).isoformat()
    }
