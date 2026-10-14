import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_retention_matrix(df):
    df['activity_month'] = pd.to_datetime(df['activity_month'])
    df['cohort_month'] = pd.to_datetime(df['cohort_month'])
    cohort_size = df.groupby('cohort_month')['user_id'].nunique().reset_index().rename(columns={'user_id': 'size'})
    df['period'] = (df['activity_month'].dt.year - df['cohort_month'].dt.year)*12+(df['activity_month'].dt.month - df['cohort_month'].dt.month)
    cohort_groups = df.groupby(['cohort_month', 'period'])['user_id'].nunique().reset_index().rename(columns={'user_id': 'count_user'})
    retention_matrix = cohort_groups.merge(cohort_size, on='cohort_month')
    retention_matrix['retention_rate'] = retention_matrix['count_user']/retention_matrix['size']
    retention_matrix['cohort_month'] = retention_matrix['cohort_month'].astype(float)
    if not {'user_id', 'cohort_month', 'activity_month'}.issubset(df.columns):
        raise ValueError("Input DataFrame must contain \"user_id\", \"cohort_month\", and \"activity_month\" columns.")
    return retention_matrix

def plot_retention_matrix(retention_matrix):
    plt.figure(figsize=(8, 5))
    sns.heatmap(
        retention_matrix,
        annot=True,
        fmt=".0f",
        cmap="YlGnBu",
        linewidths=.5,
        cbar_kws={"label": "Retention (%)"})
    plt.title("Cohort Retention Matrix Heatmap")
    plt.ylabel("Cohort (Signup Month)")
    plt.xlabel("Period Since Signup")
    plt.tight_layout()
    plt.show()


# Sample synthetic cohort data for demonstration
data = {
    "user_id": [1,1,1,2,2,3,3,4,5,6,7,7,8,8,8,9,10,10,11,11,12,13,14,15],
    "cohort_month": ["2023-01","2023-01","2023-01","2023-01","2023-01","2023-02","2023-02","2023-02","2023-02","2023-03","2023-03","2023-03","2023-03","2023-03","2023-03","2023-03","2023-04","2023-04","2023-04","2023-04","2023-04","2023-05","2023-05","2023-05"],
    "activity_month": ["2023-01","2023-02","2023-03","2023-01","2023-02","2023-02","2023-03","2023-02","2023-02","2023-03","2023-03","2023-04","2023-03","2023-04","2023-05","2023-04","2023-04","2023-05","2023-04","2023-05","2023-05","2023-05","2023-05","2023-05"]
}
df = pd.DataFrame(data)
retention_matrix = generate_retention_matrix(df)
print(retention_matrix.info())
plot_retention_matrix(retention_matrix)
