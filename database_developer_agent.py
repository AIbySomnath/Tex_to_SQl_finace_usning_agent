from smolagents import tool

@tool
def generate_sql_query(command: str) -> str:
    """
    Generates the appropriate SQL query based on the command.

    Args:
        command: The command to process.
    """
    if command == "Give me the account summary for the current month":
        query = "SELECT * FROM receipts WHERE strftime('%m', 'now') = strftime('%m', date)"
        return query
    else:
        return ""

if __name__ == "__main__":
    command = "Give me the account summary for the current month"
    print(generate_sql_query(command))