import pandas as pd

def prepare_cohort_data(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['cohort_month'] = df.groupby('user_id')['order_date'].transform('min').dt.to_period('M')
    df['cohort_index'] = (df['order_date'].dt.year - df['cohort_month'].dt.year)*12+(df['order_date'].dt.month - df['cohort_month'].dt.month)
    df['total_orders'] = df.groupby('user_id').cumcount()+1
    df['cohort_month'] = df['cohort_month'].astype(str)
    return df

# Sample data for demonstration
data = {
    'user_id': [1, 1, 2, 2, 2, 3],
    'order_id': [101, 102, 201, 202, 203, 301],
    'order_date': [
        '2024-01-15', '2024-02-10',
        '2024-01-20', '2024-03-05', '2024-03-25',
        '2024-02-01'
    ]
}
df = pd.DataFrame(data)
result = prepare_cohort_data(df)
print(result)