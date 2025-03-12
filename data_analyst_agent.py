from smolagents import tool

@tool
def analyze_data(raw_data: str) -> dict:
    """
    Analyzes the raw data to extract patterns and insights.

    Args:
        raw_data: The raw data retrieved from the SQL query.
    """
    rows = raw_data.strip().split('\n')
    insights = {
        "total_records": len(rows) - 1,
        "average_tip": sum(float(row.split(', ')[-1]) for row in rows[1:]) / (len(rows) - 1),
    }
    return insights

if __name__ == "__main__":
    raw_data = """
1, Alan Payne, 12.06, 1.20
2, Alex Mason, 23.86, 0.24
3, Woodrow Wilson, 53.43, 5.43
4, Margaret James, 21.11, 1.00
"""
    print(analyze_data(raw_data))