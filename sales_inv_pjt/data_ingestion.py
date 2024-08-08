import pandas as pd
from sqlalchemy import create_engine


# Database connection
engine = create_engine("sqlite:///sales_data.db")
query = "SELECT * FROM sales"
sales_data = pd.read_sql(query, engine)

# Data cleaning
sales_data["date"] = pd.to_datetime(sales_data["date"])
sales_data.fillna(method="ffill", inplace=True)

print(sales_data.head())
