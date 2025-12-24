from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

# 1. VERIFICATION ROUTE (Unchanged - This works)
@app.get("/.well-known/openai-apps-challenge")
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    # Your token from the latest screenshot
    return PlainTextResponse("nwgCcc8SO8zXQj1E59zeE-_1mv-V8retz1G8YpAEGK8")

# 2. MOCK TOOLS ROUTE (The Fix: Added POST support)
# We use @app.api_route to handle both GET and POST requests.
@app.api_route("/mcp/tools", methods=["GET", "POST"])
async def list_tools(request: Request):
    # We return a standard JSON-RPC empty response to make the scanner happy
    return JSONResponse(content={
        "jsonrpc": "2.0",
        "result": {
            "tools": []
        },
        "id": 1
    })

# 3. ROOT CHECK
@app.get("/")
async def home():
    return {"status": "Daily Spark - POST Handler Added"}
