import secrets
from fastapi import Header, HTTPException
from app.config import settings

def require_api_key(x_api_key: str = Header(default="")):
    expected = settings.agent_api_key
    if not expected or expected == "change-me":
        raise HTTPException(status_code=503, detail="Set a strong AGENT_API_KEY in .env")
    if not secrets.compare_digest(x_api_key, expected):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return "local-admin"
