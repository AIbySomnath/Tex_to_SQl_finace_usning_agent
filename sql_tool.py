from sqlalchemy import create_engine, text
from database import engine

def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'transactions'. Its description is as follows:
        Columns:
        - transaction_id: INTEGER
        - customer_name: VARCHAR(50)
        - transaction_amount: FLOAT
        - transaction_type: VARCHAR(20)
        - transaction_date: STRING

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output