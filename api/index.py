from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# 1. The Domain Verification Route (The most important part)
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    # This matches the token from your screenshots
    return {"verification_token": "5ZwbYcPS7n0gb_1iWrHNCQyTtIk2KQYXnBPoW2U_btE"}

# 2. A "Fake" Tools Route
# This tricks the server into thinking it's alive, preventing 404 errors
@app.get("/mcp/tools")
@app.post("/mcp/tools")
async def fake_tools():
    return JSONResponse(content={"tools": []})

# 3. Root Route (To check if it's online in browser)
@app.get("/")
async def home():
    return {"status": "Daily Spark is Online (Mock Mode)"}
