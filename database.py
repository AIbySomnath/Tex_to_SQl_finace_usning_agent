from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, insert, inspect

# Database setup with financial data
engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# Create transactions SQL table
transactions = Table(
    "transactions",
    metadata_obj,
    Column("transaction_id", Integer, primary_key=True),
    Column("customer_name", String(50)),
    Column("transaction_amount", Float),
    Column("transaction_type", String(20)),
    Column("transaction_date", String),
)
metadata_obj.create_all(engine)

# Insert data into the table
rows = [
    {"transaction_id": 1, "customer_name": "Alan Payne", "transaction_amount": 1200.06, "transaction_type": "Credit", "transaction_date": "2025-03-01"},
    {"transaction_id": 2, "customer_name": "Alex Mason", "transaction_amount": 2386.86, "transaction_type": "Debit", "transaction_date": "2025-03-05"},
    {"transaction_id": 3, "customer_name": "Woodrow Wilson", "transaction_amount": 5343.43, "transaction_type": "Credit", "transaction_date": "2025-03-10"},
    {"transaction_id": 4, "customer_name": "Margaret James", "transaction_amount": 2111.11, "transaction_type": "Debit", "transaction_date": "2025-03-12"},
    {"transaction_id": 5, "customer_name": "John Doe", "transaction_amount": 1500.00, "transaction_type": "Credit", "transaction_date": "2025-03-15"},
    {"transaction_id": 6, "customer_name": "Jane Smith", "transaction_amount": 3200.25, "transaction_type": "Debit", "transaction_date": "2025-03-18"},
    {"transaction_id": 7, "customer_name": "Emily Davis", "transaction_amount": 2100.10, "transaction_type": "Credit", "transaction_date": "2025-03-20"},
    {"transaction_id": 8, "customer_name": "Michael Brown", "transaction_amount": 4500.50, "transaction_type": "Debit", "transaction_date": "2025-03-22"},
    {"transaction_id": 9, "customer_name": "Sarah Wilson", "transaction_amount": 3700.75, "transaction_type": "Credit", "transaction_date": "2025-03-25"},
    {"transaction_id": 10, "customer_name": "David Johnson", "transaction_amount": 2950.60, "transaction_type": "Debit", "transaction_date": "2025-03-28"},
    {"transaction_id": 11, "customer_name": "Chris Lee", "transaction_amount": 1980.40, "transaction_type": "Credit", "transaction_date": "2025-03-02"},
    {"transaction_id": 12, "customer_name": "Jessica Taylor", "transaction_amount": 2750.90, "transaction_type": "Debit", "transaction_date": "2025-03-06"},
    {"transaction_id": 13, "customer_name": "Matthew Martinez", "transaction_amount": 3100.12, "transaction_type": "Credit", "transaction_date": "2025-03-11"},
    {"transaction_id": 14, "customer_name": "Ashley White", "transaction_amount": 4200.35, "transaction_type": "Debit", "transaction_date": "2025-03-13"},
    {"transaction_id": 15, "customer_name": "Brian Harris", "transaction_amount": 3850.55, "transaction_type": "Credit", "transaction_date": "2025-03-16"},
    {"transaction_id": 16, "customer_name": "Olivia Lewis", "transaction_amount": 4900.75, "transaction_type": "Debit", "transaction_date": "2025-03-19"},
    {"transaction_id": 17, "customer_name": "James Walker", "transaction_amount": 2700.90, "transaction_type": "Credit", "transaction_date": "2025-03-21"},
    {"transaction_id": 18, "customer_name": "Sophia Hall", "transaction_amount": 3500.40, "transaction_type": "Debit", "transaction_date": "2025-03-24"},
    {"transaction_id": 19, "customer_name": "Daniel Allen", "transaction_amount": 4100.60, "transaction_type": "Credit", "transaction_date": "2025-03-27"},
    {"transaction_id": 20, "customer_name": "Ella Young", "transaction_amount": 2600.80, "transaction_type": "Debit", "transaction_date": "2025-03-30"},
    {"transaction_id": 21, "customer_name": "Liam King", "transaction_amount": 1400.10, "transaction_type": "Credit", "transaction_date": "2025-03-03"},
    {"transaction_id": 22, "customer_name": "Mia Wright", "transaction_amount": 3300.20, "transaction_type": "Debit", "transaction_date": "2025-03-07"},
    {"transaction_id": 23, "customer_name": "Noah Scott", "transaction_amount": 1800.30, "transaction_type": "Credit", "transaction_date": "2025-03-09"},
    {"transaction_id": 24, "customer_name": "Ava Green", "transaction_amount": 2900.40, "transaction_type": "Debit", "transaction_date": "2025-03-14"},
    {"transaction_id": 25, "customer_name": "Lucas Adams", "transaction_amount": 3700.50, "transaction_type": "Credit", "transaction_date": "2025-03-17"},
    {"transaction_id": 26, "customer_name": "Amelia Baker", "transaction_amount": 2500.60, "transaction_type": "Debit", "transaction_date": "2025-03-23"},
    {"transaction_id": 27, "customer_name": "Benjamin Nelson", "transaction_amount": 3200.70, "transaction_type": "Credit", "transaction_date": "2025-03-26"},
    {"transaction_id": 28, "customer_name": "Charlotte Carter", "transaction_amount": 2300.80, "transaction_type": "Debit", "transaction_date": "2025-03-29"},
    {"transaction_id": 29, "customer_name": "Henry Mitchell", "transaction_amount": 3100.90, "transaction_type": "Credit", "transaction_date": "2025-03-31"},
    {"transaction_id": 30, "customer_name": "Isabella Perez", "transaction_amount": 2700.11, "transaction_type": "Debit", "transaction_date": "2025-03-04"},
    {"transaction_id": 31, "customer_name": "Ethan Roberts", "transaction_amount": 3600.22, "transaction_type": "Credit", "transaction_date": "2025-03-08"},
    {"transaction_id": 32, "customer_name": "Abigail Turner", "transaction_amount": 2900.33, "transaction_type": "Debit", "transaction_date": "2025-03-10"},
    {"transaction_id": 33, "customer_name": "Alexander Phillips", "transaction_amount": 2500.44, "transaction_type": "Credit", "transaction_date": "2025-03-12"},
    {"transaction_id": 34, "customer_name": "Emily Campbell", "transaction_amount": 3400.55, "transaction_type": "Debit", "transaction_date": "2025-03-14"},
    {"transaction_id": 35, "customer_name": "Joshua Parker", "transaction_amount": 2800.66, "transaction_type": "Credit", "transaction_date": "2025-03-16"},
    {"transaction_id": 36, "customer_name": "Madison Evans", "transaction_amount": 3700.77, "transaction_type": "Debit", "transaction_date": "2025-03-18"},
    {"transaction_id": 37, "customer_name": "Oliver Edwards", "transaction_amount": 3000.88, "transaction_type": "Credit", "transaction_date": "2025-03-20"},
    {"transaction_id": 38, "customer_name": "Sofia Collins", "transaction_amount": 2200.99, "transaction_type": "Debit", "transaction_date": "2025-03-22"},
    {"transaction_id": 39, "customer_name": "Andrew Stewart", "transaction_amount": 2100.10, "transaction_type": "Credit", "transaction_date": "2025-03-24"},
    {"transaction_id": 40, "customer_name": "Ella Morris", "transaction_amount": 3300.20, "transaction_type": "Debit", "transaction_date": "2025-03-26"},
    {"transaction_id": 41, "customer_name": "William Rogers", "transaction_amount": 2000.30, "transaction_type": "Credit", "transaction_date": "2025-03-28"},
    {"transaction_id": 42, "customer_name": "Grace Cook", "transaction_amount": 2800.40, "transaction_type": "Debit", "transaction_date": "2025-03-30"},
    {"transaction_id": 43, "customer_name": "James Bell", "transaction_amount": 2600.50, "transaction_type": "Credit", "transaction_date": "2025-03-01"},
    {"transaction_id": 44, "customer_name": "Avery Murphy", "transaction_amount": 2400.60, "transaction_type": "Debit", "transaction_date": "2025-03-03"},
    {"transaction_id": 45, "customer_name": "Mason Bailey", "transaction_amount": 2200.70, "transaction_type": "Credit", "transaction_date": "2025-03-05"},
    {"transaction_id": 46, "customer_name": "Samantha Rivera", "transaction_amount": 2000.80, "transaction_type": "Debit", "transaction_date": "2025-03-07"},
    {"transaction_id": 47, "customer_name": "Michael Cooper", "transaction_amount": 1800.90, "transaction_type": "Credit", "transaction_date": "2025-03-09"},
    {"transaction_id": 48, "customer_name": "Elizabeth Richardson", "transaction_amount": 1600.10, "transaction_type": "Debit", "transaction_date": "2025-03-11"},
    {"transaction_id": 49, "customer_name": "Daniel Barnes", "transaction_amount": 1400.20, "transaction_type": "Credit", "transaction_date": "2025-03-13"},
    {"transaction_id": 50, "customer_name": "Sophia Ross", "transaction_amount": 1200.30, "transaction_type": "Debit", "transaction_date": "2025-03-15"},
]
for row in rows:
    stmt = insert(transactions).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)

# Print table description
inspector = inspect(engine)
columns_info = [(col["name"], col["type"]) for col in inspector.get_columns("transactions")]
table_description = "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
print(table_description)