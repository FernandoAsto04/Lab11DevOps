from core import payload

def test_payload():
    data = payload()
    assert data["ok"] is True
    assert "ts" in data