# Importing required libraries
from sys import getrefcount
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Importing csv file
df = pd.read_csv("/Users/gopalsharma/Documents/Python/MFST/Task_6/disney_plus_titles.csv")
# Displaying top 10 rows of the dataset
print(df.head(10))
# Displaying last 10 rows of the dataset
print(df.tail(10))
# Displaying shape of dataset (Number of rows and column)
print(df.shape)
print('Number of Rows:', df.shape[0])
print('Number of Columns:', df.shape[1])
# Displaying information of dataset
print(df.info())
# Checking for missiong value
print('Any missiong value?', df.isnull().values.any())
print(df.isnull().sum())
sns.heatmap(df.isnull())
# plt.show()
# Checking for duplicate
dup_df = df.duplicated().any()
print('Are there any duplicate values?', dup_df)
# Overall statistics of DataFrame
print(df.describe(include='all'))
# Identifying valid (non-missing) data in dataframe (Boolean values)
print(df.notnull())
# Identifying valid (non-missing) data in each column of dataframe (True values)
print(df.notnull().sum())
# Identifying the total number of valid (non-missing) data in dataframe
print(df.notnull().sum().sum())
# Filling missing values with a specific value
df2 = df.fillna(value=0)
print(df2)
# Line chart - Time Series Analysis
count_df = df.groupby(['release_year', 'type']).size().reset_index(name='count')
pivot_df = count_df.pivot(index='release_year', columns='type', values='count').fillna(0)
plt.figure(figsize=(10, 6))
sns.lineplot(data=pivot_df, markers=True)
plt.title('Number of Movies and TV Shows Over the Years on Disney Plus')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.legend(title='Type of Show')
plt.grid(True)
plt.show()
# Comparing of genres of entertainment involved in dataset
plt.figure(figsize=(10, 6))
type = df['type'].value_counts()
plt.pie(type, labels=type.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Genre')
plt.axis('equal')
plt.show()
# Checking rating distribution
plt.figure(figsize=(10,6))
sns.countplot(df['rating'])
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()
# Testing separation of data wseparated by commas
df['director'] = df['director'].str.split(',')
df_director = df.explode('director')
print("Data after separating genres:")
print(df_director)
# Plotting pie chart for distribution of genre
genres = df['listed_in'].str.split(',').explode().str.strip()
genre_counts = genres.value_counts()
plt.figure(figsize=(10, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Genres')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
# Plotting release year distribution
sns.displot(x='release_year', data=df, kde=True)
plt.show()
# Plotting rating distribution
sns.countplot(x='rating', data=df, hue='type')
plt.show()
#Filtering TV Show details
print(df[df['type'] == 'TV Show'])
# Filtering Movie details
print(df[df['type'] == 'Movie'])
# Seasons Distribution of TV Shows
sns.countplot(y='duration', data=df[df['type'] == 'TV Show'], palette = 'dark:salmon_r')
plt.title('Seasons Distribution of TV Shows')
plt.show()
# Frequent Director Distribution
plt.figure(figsize=(12, 10))
print(df[df['type'] == 'Movie'].director.value_counts()[:8].plot(kind='bar', color='salmon'))
plt.show()