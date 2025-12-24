from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# 1. VERIFICATION ROUTE (With your NEW Token)
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    # Token taken from image_55adc5.png
    return {"verification_token": "nwgcCc8SO8zXQj1E59zeE-_1mv-V8retz1G8YpAEGK8"}

# 2. IMPROVED MOCK TOOLS
# We return a dummy tool so ChatGPT sees "something" and turns Green
@app.get("/mcp/tools")
async def list_tools():
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

# 3. ROOT CHECK
@app.get("/")
async def home():
    return {"status": "Daily Spark is Online"}
