import pandas as pd

# Sample user signup data
data = {
    "user_id": [201, 202, 201, 203, 204, 202, 205],
    "signup_date": [
        "2024-04-01", "2024-04-03", "2024-04-07",
        "2024-04-10", "2024-04-15", "2024-04-04", "2024-04-20"
    ]
}

df = pd.DataFrame(data)

# Convert 'signup_date' to datetime
df["signup_date"] = pd.to_datetime(df["signup_date"])
df['cohort_week'] = df.groupby('user_id')['signup_date'].transform('min').dt.to_period('W')

print(df)