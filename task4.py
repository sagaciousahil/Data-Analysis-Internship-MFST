# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
# Loading csv file
df = pd.read_csv("/Users/gopalsharma/Documents/Python/MFST/Task_4/USvideos.csv")
# Printing first five rows
print(df.head())
# Checking dimensions of DataFrame
print(df.shape)
# Removing duplicate entries
df = df.drop_duplicates()
# Re-checking dimensions of DataFrame
print(df.shape)
# Summary of descriptive statistics for numerical columns
print(df.describe())
# Concise summary of DataFrame
print(df.info())
# Dropping columns
columns_to_remove = ['thumbnail_link', 'description']
df = df.drop(columns=columns_to_remove)
print(df.info())
# Converting strings to datetime objects using a specific date format through datetime module
import datetime
df['trending_date'] = df['trending_date'].apply(lambda x: datetime.datetime.strptime(x, '%y.%d.%m'))
print(df.head(3))
# Converting strings to datetime objects using a specific date format through datetime module
df['publish_time'] = pd.to_datetime(df['publish_time'])
print(df['publish_time'])
# Extracts the month, day and hour from 'publish_time' column
df['publish_month'] = df['publish_time'].dt.month
df['publish_day'] = df['publish_time'].dt.day
df['publish_hour'] = df['publish_time'].dt.hour
print(df['publish_month'])
print(df['publish_hour'])
print(df['publish_day'])
# Sorted Unique Values of 'category_id'
print(sorted(df['category_id'].unique()))
# Initializing the 'category_name' Column with NaN (Not a Number)
df['category_name'] = np.nan
# Assigning Category Names Based on 'category_id'
df.loc[(df["category_id"] == 1), "category_name"] = 'Film and Animation'
df.loc[(df["category_id"] == 2), "category_name"] = 'Autos and Vehicles'
df.loc[(df["category_id"] == 10), "category_name"] = 'Music'
df.loc[(df["category_id"] == 15), "category_name"] = 'Pets and Animals'
df.loc[(df["category_id"] == 17), "category_name"] = 'Sports'
df.loc[(df["category_id"] == 19), "category_name"] = 'Travel and Events'
df.loc[(df["category_id"] == 20), "category_name"] = 'Gaming'
df.loc[(df["category_id"] == 22), "category_name"] = 'People and Blogs'
df.loc[(df["category_id"] == 23), "category_name"] = 'Comedy'
df.loc[(df["category_id"] == 24), "category_name"] = 'Entertainment'
df.loc[(df["category_id"] == 25), "category_name"] = 'News and Politics'
df.loc[(df["category_id"] == 26), "category_name"] = 'How to and Style'
df.loc[(df["category_id"] == 27), "category_name"] = 'Education'
df.loc[(df["category_id"] == 28), "category_name"] = 'Science and Technology'
df.loc[(df["category_id"] == 29), "category_name"] = 'Non Profits and Activism'
df.loc[(df["category_id"] == 30), "category_name"] = 'Movies'
df.loc[(df["category_id"] == 43), "category_name"] = 'Shows'
print(df.head())
# --- Bar Chart of Total Publish Video Per Year
# Extracting year from 'publish_time'
df['year'] = df['publish_time'].dt.year
# Grouping by Year and Counts Videos
yearly_counts = df.groupby('year')['video_id'].count()
# Plotting the Yearly Counts as a Bar Chart
yearly_counts.plot(kind='bar', xlabel='Year', ylabel='Total Publish Count', title='Total Publish Video Per Year')
plt.show()
# --- Bar Chart of Total Views Per Year
# Grouping by Year and Sums Views
yearly_views = df.groupby('year')['views'].sum()
# Plotting the Yearly Views as a Bar Chart
yearly_views.plot(kind='bar', xlabel='Year', ylabel='Total Views', title='Total Views Per Year')
# Rotating the X-axis Tick Labels
plt.xticks(rotation=0)
# Adjusting the layout
plt.tight_layout()
plt.show()
# --- Bar Chart of Top 5 Categories
# Grouping by Category and Sum Views
category_views = df.groupby('category_name')['views'].sum().reset_index()
# Sorting 'category_views' in descending order
top_categories = category_views.sort_values(by='views', ascending=False).head(5)
plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel('Category Name', fontsize=12)
plt.ylabel('Total Views', fontsize=12)
plt.title('Top 5 Categories', fontsize=15)
plt.tight_layout()
plt.show()
# --- Count Plot of Video Count by Category
# Creating a new figure with a specified size of 12 inches in width and 6 inches in height
plt.figure(figsize=(12,6))
sns.countplot(x='category_name', data=df, order=df['category_name'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Video Count by Category')
plt.show()
# --- Bar Plot of Number of Videos Published Per Hour
videos_per_hour = df['publish_hour'].value_counts().sort_index()
plt.figure(figsize=(12,6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, palette='rocket')
plt.title('Number of Videos Published Per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()
# --- Line Plot of Videos Published Over Time
df['publish_time'] = pd.to_datetime(df['publish_time'])
df['publish_date'] = df ['publish_time'].dt.date
video_count_by_date = df.groupby('publish_date').size()
plt.figure(figsize=(12, 6))
sns.lineplot(data=video_count_by_date)
plt.title('Videos Published Over Time')
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()
# --- Scatter plot between 'views' and 'Likes'
sns.scatterplot(data=df, x= 'views', y='likes')
plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()
# Comprehensive visualization consisting of four subplots arranged in a 2x2 grid
plt.figure(figsize=(14,8))
plt.subplots_adjust(wspace=0.2, hspace=0.4, top=0.9)
plt.subplot(2,2,1)
g = sns.countplot(x='comments_disabled', data=df)
g.set_title("Comments Disabled", fontsize=16)
plt.subplot(2,2,2)
g1 = sns.countplot(x='ratings_disabled', data=df)
g1.set_title("Rating Disabled", fontsize=16)
plt.subplot(2,2,3)
g2 = sns.countplot(x='video_error_or_removed', data=df)
g2.set_title("Video Error or Removed", fontsize=16)
plt.show()
# Correlation between 'views' and 'likes'
corr_matrix = df['views'].corr(df['likes'])
print(corr_matrix)