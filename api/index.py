from mcp.server.fastmcp import FastMCP
import random

# 1. Initialize FastMCP
mcp = FastMCP("Daily Spark")

# 2. Define Tools (This fixes the "Tool scan failed" error)
@mcp.tool()
def get_daily_quote() -> str:
    """Returns an inspiring quote."""
    return random.choice(["Quote A", "Quote B", "Quote C"])

@mcp.tool()
def get_daily_fact() -> str:
    """Returns a fun fact."""
    return random.choice(["Fact A", "Fact B", "Fact C"])

# 3. EXPOSE THE APP FOR VERCEL
app = mcp._http_server

# 4. Verification Route
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    # Using the token you confirmed
    return {"verification_token": "5ZwbYcPS7n0gb_1iWrHNCQyTtIk2KQYXnBPoW2U_btE"}
