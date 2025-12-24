from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

# 1. VERIFICATION ROUTE (Strict Plain Text)
@app.get("/.well-known/openai-apps-challenge")
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    # Your token from the screenshots
    return PlainTextResponse("nwgCcc8SO8zXQj1E59zeE-_1mv-V8retz1G8YpAEGK8")

# 2. MOCK TOOLS (Empty list to satisfy the scanner)
@app.get("/mcp/tools")
async def list_tools():
    return JSONResponse(content={"tools": []})

# 3. ROOT CHECK
@app.get("/")
async def home():
    return {"status": "Daily Spark - Final Attempt"}
