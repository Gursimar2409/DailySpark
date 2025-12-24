from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
import random

# 1. Initialize FastMCP
mcp = FastMCP("Daily Spark")

# 2. Define your tools (Same as before)
@mcp.tool()
def get_daily_quote() -> str:
    """Returns an inspiring quote for the day."""
    quotes = [
        "The best way to predict the future is to create it.",
        "Do what you can, with what you have, where you are.",
        "Happiness is not something ready made. It comes from your own actions."
    ]
    return random.choice(quotes)

@mcp.tool()
def get_daily_fact() -> str:
    """Returns a fascinating random fact."""
    facts = [
        "Honey never spoils. You can eat honey found in Egyptian tombs.",
        "A day on Venus is longer than a year on Venus.",
        "Bananas are berries, but strawberries are not."
    ]
    return random.choice(facts)

# 3. EXPOSE THE APP FOR VERCEL (Crucial Step)
# This extracts the internal web server so Vercel can see it
app = mcp._http_server

# 4. Add the Domain Verification Route
# ChatGPT needs this specific path to verify you own the site
@app.get("/.well-known/openai/verification-token")
async def verify_domain():
    return {"verification_token": "5ZwbYcPS7n0gb_1iWrHNCQyTtIk2KQYXnBPoW2U_btE"}
