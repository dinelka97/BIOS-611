import pandas as pd 
import polars as pls

df = pd.read_csv("episode_word_counts.csv")

n_rows = df.shape[0]
row_sums = df.select_dtypes(include='number').sum(axis=1)

print("Number of Rows: ", n_rows)
print("Row Sums: ", row_sums)

df['row_sum'] = row_sums

df_filt = df[df['row_sum'] >= 100]

df_filt.to_csv("q5.csv", index=False)