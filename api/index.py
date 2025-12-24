from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()

# --- 1. DOMAIN VERIFICATION (Strict Mode) ---
@app.get("/.well-known/openai-apps-challenge")
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    # We define the token as a variable to prevent copy-paste errors
    # VERIFY THIS MATCHES YOUR FORM EXACTLY:
    my_token = "nwgCcc8SO8zXQj1E59zeE-_1mv-V8retz1G8YpAEGK8"
    
    return Response(content=my_token, media_type="text/plain")

# --- 2. MOCK TOOLS ---
@app.get("/mcp/tools")
@app.post("/mcp/tools")
async def list_tools():
    return JSONResponse(content={
        "tools": [{
            "name": "get_daily_quote",
            "description": "Returns a random inspiring quote.",
            "inputSchema": {"type": "object", "properties": {}, "required": []}
        }]
    })

# --- 3. ROOT CHECK ---
@app.get("/")
async def home():
    # Changing this text forces Vercel to create a new build (busting the cache)
    return {"status": "Daily Spark - Verifying Domain Attempt 2"}
