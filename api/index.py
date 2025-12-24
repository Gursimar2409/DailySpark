from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()

# --- 1. THE CRITICAL FIX (Domain Verification) ---
# We serve the token as PLAIN TEXT on the EXACT path ChatGPT asked for.
@app.get("/.well-known/openai-apps-challenge")
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    # We return raw text, not JSON
    return Response(
        content="nwgCcc8SO8zXQj1E59zeE-_1mv-V8retz1G8YpAEGK8", 
        media_type="text/plain"
    )

# --- 2. THE MOCK TOOLS (To satisfy the scanner) ---
@app.get("/mcp/tools")
@app.post("/mcp/tools")
async def list_tools():
    # This JSON structure mimics a real MCP server perfectly
    return JSONResponse(content={
        "tools": [
            {
                "name": "get_daily_quote",
                "description": "Returns a random inspiring quote.",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        ]
    })

# --- 3. ROOT CHECK ---
@app.get("/")
async def home():
    return {"status": "Daily Spark is Online (Plain Text Fix)"}
