from smolagents import tool

@tool
def generate_report(insights: dict) -> str:
    """
    Generates a human-readable report based on the insights.

    Args:
        insights: The insights extracted from the raw data.
    """
    report = (
        f"Summary for the current month:\n"
        f"Total Records: {insights['total_records']}\n"
        f"Average Tip: ${insights['average_tip']:.2f}\n"
    )
    return report

if __name__ == "__main__":
    insights = {
        "total_records": 4,
        "average_tip": 1.97,
    }
    print(generate_report(insights))