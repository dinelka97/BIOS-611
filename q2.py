import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("episode_word_counts.csv")

### (i) histogram

col_sums = list(df.select_dtypes(include='number').sum())   ## subset to only the numeric columns

data = {
  'word': df.columns[1:],
  'count': col_sums
}

df_new = pd.DataFrame(data, index=list(range(df.shape[1]-1)))

## subset to having a count of 1000 or more
df_new = df_new[df_new['count'] >= 1000]

## arrange in descending order

df_new = df_new.sort_values(by='count', ascending=False)

## create a bar plot (hist doesnt really make sense here)

plt.figure(figsize=(10, 6))
plt.bar(df_new['word'], df_new['count'], color='skyblue', edgecolor='black')

# Customize the plot
plt.title('Bar Plot - word count')
plt.xlabel('word')
plt.ylabel('count')
plt.xticks(rotation=90)  # Rotate category names for better visibility
plt.grid(axis='y')

# Show the plot
plt.savefig('word_count.png', dpi=300, bbox_inches='tight')

### (ii) PCA

# parameters
n_pcs = 2

df_num = df.select_dtypes(include='number')   ## subset to only the numeric columns

## performing dimension reduction

scaler = StandardScaler()
standardized_data = scaler.fit_transform(df_num)

# perform PCA. I want to reduce it to 10 dimensions
pca = PCA(n_components=n_pcs) 
principal_components = pca.fit_transform(standardized_data)

# df for the PCs
pca_df = pd.DataFrame(data=principal_components, columns=[f'PC{i}' for i in range(1, n_pcs + 1)])

# finding the proportion of variance explained

explained_variance = pca.explained_variance_ratio_
tot_var = sum(explained_variance)
print("Total Variance Explained:", tot_var) 

plt.figure(figsize=(8, 6))
plt.scatter(pca_df['PC1'], pca_df['PC2'])
plt.title('PCA Result')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid()

plt.savefig('pca.png', dpi=300, bbox_inches='tight')


