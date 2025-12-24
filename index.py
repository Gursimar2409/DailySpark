from mcp.server.fastmcp import FastMCP
import random

# Initialize FastMCP
mcp = FastMCP("Daily Spark")

# Define Tools
@mcp.tool()
def get_daily_quote() -> str:
    return random.choice(["Quote 1", "Quote 2", "Quote 3"])

@mcp.tool()
def get_daily_fact() -> str:
    return random.choice(["Fact 1", "Fact 2", "Fact 3"])

# EXPOSE THE APP FOR VERCEL
app = mcp._http_server

# Verification Route (Placeholder for now)
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    return {"verification_token": "5ZwbYcPS7n0gb_1iWrHNCQyTtIk2KQYXnBPoW2U_btE"}