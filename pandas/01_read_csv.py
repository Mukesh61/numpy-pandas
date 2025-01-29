import pandas as pd

df = pd.read_csv('sample_loan.csv')

# filter only where loan amount > 10

df_loan_gt_10 = df[df['loan_amount'] > 10]

total = 0
for _, row in df.iterrows():
  if row['loan_status'] == 'Completed':
    total += 1

len(df[df['loan_status']=='Completed'])

