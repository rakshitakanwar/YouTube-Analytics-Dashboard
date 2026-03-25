

import pandas as pd

# Load dataset
df = pd.read_csv('/content/youtube.csv')

# Show data
print(df.head())

print("Shape:", df.shape)
print("Columns:", df.columns)

# Remove missing values
df.dropna(inplace=True)

# Create engagement column
df['engagement'] = (df['likes'] + df['comment_count']) / df['views']

# Top categories
if 'category_id' in df.columns:
    print(df.groupby('category_id')['views'].mean().sort_values(ascending=False).head())

# Save file
df.to_csv('/content/final_data.csv', index=False)

print("Done ✅")

import matplotlib.pyplot as plt
import seaborn as sns

# Top 10 videos by views
top_videos = df.sort_values(by='views', ascending=False).head(10)

plt.figure()
sns.barplot(x=top_videos['views'], y=top_videos['title'])
plt.title("Top 10 Videos by Views")
plt.show()

# Category wise average views
plt.figure()
df.groupby('category_id')['views'].mean().plot(kind='bar')
plt.title("Category vs Avg Views")
plt.show()

# Engagement distribution
plt.figure()
sns.histplot(df['engagement'], bins=30)
plt.title("Engagement Distribution")
plt.show()