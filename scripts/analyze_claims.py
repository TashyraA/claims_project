import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure charts folder exists
os.makedirs("../charts", exist_ok=True)

# -----------------------------
# Load data from SQLite
# -----------------------------
conn = sqlite3.connect("../data/claims.db")
df = pd.read_sql_query("SELECT * FROM claims", conn)
conn.close()

# -----------------------------
# KPI calculations
# -----------------------------
total_claims = len(df)
total_paid = df['Amount'].sum()
avg_paid = df['Amount'].mean()
top_claims = df.sort_values('Amount', ascending=False).head(10)

claims_by_type = df.groupby('ClaimType')['Amount'].agg(['count', 'sum'])
claims_by_region = df.groupby('Region')['Amount'].agg(['count', 'sum'])

# Print KPIs
print(f"Total Claims: {total_claims}")
print(f"Total Paid: ${total_paid:,.2f}")
print(f"Average Claim Paid: ${avg_paid:,.2f}\n")

print("Claims by Type:")
print(claims_by_type, "\n")

print("Claims by Region:")
print(claims_by_region, "\n")

print("Top 10 Claims:")
print(top_claims)

# -----------------------------
# Visualization
# -----------------------------
# Total Paid by Claim Type
claims_by_type['sum'].plot(kind='bar', title='Total Paid by Claim Type')
plt.ylabel('Total Paid ($)')
plt.savefig("../charts/total_paid_by_type.png")
plt.close()

# Total Paid by Region
claims_by_region['sum'].plot(kind='bar', title='Total Paid by Region', color='green')
plt.ylabel('Total Paid ($)')
plt.savefig("../charts/total_paid_by_region.png")
plt.close()

# Optional: Top claims chart
top_claims.plot(kind='bar', x='ClaimID', y='Amount', title='Top 10 Claims', legend=False)
plt.ylabel('Claim Amount ($)')
plt.savefig("../charts/top_10_claims.png")
plt.close()

print("✅ KPIs calculated and charts saved to charts/ folder")
