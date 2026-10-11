import pandas as pd

def calculate_cohort_metrics(df):
    months = sorted([c for c in df.columns if c.startswith("month_")],
                    key=lambda x: int(x.split("_")[1]))
    cohorts = len(df['user_id'])
    retention_rate = []
    churn_rate = []
    survival_rate = []
    
    for i, von in enumerate(months):
        active = df[von].sum()
        retention = active / cohorts
        retention_rate.append(retention)
        churn_rate.append(1 - retention)
        survivals = (df[months[:i+1]].all(axis=1).sum())/cohorts
        survival_rate.append(survivals)

    return retention_rate, churn_rate, survival_rate

data = {
    "user_id": [1, 2, 3, 4, 5],
    "month_0": [1, 1, 1, 1, 1],  # Everyone starts active
    "month_1": [1, 0, 1, 0, 1],  # 3 users active
    "month_2": [1, 0, 0, 0, 0],  # 1 user active
}
df = pd.DataFrame(data)
print(df)

res = calculate_cohort_metrics(df)
print(res)

