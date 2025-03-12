from smolagents import tool, CodeAgent
from sql_tool import sql_engine
from model import model

@tool
def generate_sql_query(command: str) -> dict:
    """
    Generates the appropriate SQL query, executes it, and returns the result.

    Args:
        command: The command to process.
    """
    if command == "Give me the account summary for the current month":
        query = "SELECT * FROM receipts WHERE strftime('%m', 'now') = strftime('%m', date)"
        raw_data = sql_engine(query)
        summary = f"Summary: Retrieved {len(raw_data.splitlines()) - 1} records for the current month."
        return {"data": raw_data, "summary": summary}
    else:
        return {"data": "Unknown command.", "summary": "Unknown command."}

agent2 = CodeAgent(
    tools=[generate_sql_query],
    model=model,
)