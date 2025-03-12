from smolagents import tool, CodeAgent
from model import model
from database_developer_agent import generate_sql_query
from data_analyst_agent import analyze_data
from report_writer_agent import generate_report
from sql_tool import sql_engine

@tool
def process_command(command: str) -> str:
    """
    Processes the command and coordinates with other agents to generate the final response.

    Args:
        command: The command to process.
    """
    if command == "Give me the account summary for the current month":
        sql_query = generate_sql_query(command)
        raw_data = sql_engine(sql_query)
        insights = analyze_data(raw_data)
        report = generate_report(insights)
        return f"Raw Data: {raw_data}\nSummary: {report}"
    else:
        return "Unknown command."

def main(command: str):
    response = process_command(command)
    return response

if __name__ == "__main__":
    command = "Give me the account summary for the current month"
    response = main(command)
    print(response)