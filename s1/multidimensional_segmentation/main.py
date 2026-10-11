import pandas as pd

# Sample data where each (signup_month, acquisition_channel) pair has exactly one user
data = {
    "user_id": [1, 2, 3, 4, 5, 6],
    "signup_date": [
        "2023-01-15", "2023-01-15", "2023-01-25",
        "2023-02-10", "2023-02-15", "2023-02-18"
    ],
    "acquisition_channel": [
        "Email", "Ad", "Social",
        "Email", "Ad", "Social"
    ]
}

df = pd.DataFrame(data)
df["signup_month"] = pd.to_datetime(df["signup_date"]).dt.to_period("M")
print(df)

# Perform multi-dimensional cohort segmentation by signup_month and acquisition_channel
# Group by signup_month and acquisition_channel, count unique user_ids for each cohort,
# and store the result in a DataFrame named 'cohorts' with columns:
# 'signup_month', 'acquisition_channel', 'num_users'
cohorts = df.groupby(['signup_month', 'acquisition_channel'])['user_id'].nunique().reset_index().rename(columns={'user_id': 'num_users'})
print(cohorts)