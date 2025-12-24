from mcp.server.fastmcp import FastMCP
import random

# Initialize the server
mcp = FastMCP("Daily Spark")

# TOOL 1: Get a Daily Quote
@mcp.tool()
def get_daily_quote() -> str:
    """Returns an inspiring quote for the day."""
    quotes = [
        "The best way to predict the future is to create it.",
        "Do what you can, with what you have, where you are.",
        "Happiness is not something ready made. It comes from your own actions."
    ]
    return random.choice(quotes)

# TOOL 2: Get a Fun Fact
@mcp.tool()
def get_daily_fact() -> str:
    """Returns a fascinating random fact."""
    facts = [
        "Honey never spoils. You can eat honey found in Egyptian tombs.",
        "A day on Venus is longer than a year on Venus.",
        "Bananas are berries, but strawberries are not."
    ]
    return random.choice(facts)

if __name__ == "__main__":
    # This runs the server
    mcp.run()