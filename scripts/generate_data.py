import pandas as pd
import numpy as np
import random

# Parameters
n = 500  # number of rows

# Possible values
regions = ["North", "South", "East", "West"]
claim_types = ["Auto", "Health", "Property", "Workers Comp"]

# Generate data
np.random.seed(42)
data = {
    "ClaimID": range(1, n + 1),
    "Date": pd.date_range(start="2023-01-01", periods=n, freq="D"),
    "Region": [random.choice(regions) for _ in range(n)],
    "ClaimType": [random.choice(claim_types) for _ in range(n)],
    "Amount": np.random.randint(500, 20000, size=n)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("../data/claims_data.csv", index=False)

print("✅ claims_data.csv generated in data/ folder")
