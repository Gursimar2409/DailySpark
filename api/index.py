from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()

# 1. VERIFICATION ROUTE (Must stay exactly like this)
@app.get("/.well-known/openai-apps-challenge")
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    # Your correct token
    my_token = "nwgCcc8SO8zXQj1E59zeE-_1mv-V8retz1G8YpAEGK8"
    return Response(content=my_token, media_type="text/plain")

# 2. TOOLS ROUTE (Simplified to prevent "Unknown Error")
# We return an empty list. This is valid and safer.
@app.get("/mcp/tools")
@app.post("/mcp/tools")
async def list_tools():
    return JSONResponse(content={"tools": []})

# 3. ROOT CHECK
@app.get("/")
async def home():
    return {"status": "Daily Spark - Final Fix"}
