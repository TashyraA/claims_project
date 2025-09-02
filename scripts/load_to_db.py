import sqlite3
import pandas as pd

# Load CSV
df = pd.read_csv("../data/claims_data.csv")

# Connect to SQLite (creates database if it doesn't exist)
conn = sqlite3.connect("../data/claims.db")
cursor = conn.cursor()

# Load dataframe into SQLite table called 'claims'
df.to_sql("claims", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("✅ CSV loaded into claims.db")
