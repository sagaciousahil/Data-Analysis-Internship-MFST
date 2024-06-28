# Importing required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Importing csv file
df = pd.read_csv("/Users/gopalsharma/Documents/Python/MFST/tASK_5/heart.csv")
# Checking first five rows
print(df.head())
# Checking last five rows
print(df.tail())
# Checking column names
print(df.columns.values)
# Checking for null values
print(df.isna().sum())
# Checking concise summary of dataset
print(df.info())
# Plotting histogram of all numeric values
df.hist(bins=50, grid=False, figsize=(11,9))
plt.show()
# Generating descriptive statistics
print(df.describe())
# Questions
questions = ["1. How many people have heart disease and how many people dowsn't have heart disease?"
             "2. People of which sex has more heart disease?"
             "3. People of which sex has which type of chest pain most?"
             "4. People with which chest pain are most pron to have heart disease?"
             "5. Do people with higher blood pressure (trestbps) tend to have higher cholesterol (chol)?"
             "6. Does resting blood pressure are different in different age groups?"
             "7. What is the relationship between slop and target?"]
# --- 1. How many people have heart disease and how many people dowsn't have heart disease?
# Checking the values
print(df.target.value_counts())
# Plotting a bar chart
df.target.value_counts().plot(kind='bar', color=["orchid", "salmon"])
plt.title("Heart Disease Value")
plt.xlabel("1 = Heart disease, 0 = No heart disease")
plt.ylabel("Amount")
plt.show()
# Plotting a pie chart
df.target.value_counts().plot(kind='pie', figsize=(8,6))
plt.legend(["Disease", "No Disease"])
plt.show()
# '0' represent 'Female'
# '1' represent 'Male'
# '0' represent 'No Disease'
# '1' represent 'Disease'
# Checking 'Male and 'Female' in the dataset
print(df.sex.value_counts())
# Plotting a pie chart
df.sex.value_counts().plot(kind='pie', figsize=(8,6))
plt.title('Male Female Ratio')
plt.legend(['Male', 'Female'])
plt.show()
# --- 2. People of which sex has more heart disease?
print(pd.crosstab(df.target, df.sex))
# Plotting a countplot
sns.countplot(x='target', data=df, hue='sex')
plt.title("Heart Disease Frequency for Sex")
plt.xlabel("0 = No heart disease, 1 = Heart disease")
plt.show()
# Number of male is more than double in our dataset than female
# More than '45% male' has heart disease and '75% female' has heart disease
# # --- 3. People of which sex has which type of chest pain most?
# Counting values for different chest pain
print(df.cp.value_counts())
# Plotting a bar chart
df.cp.value_counts().plot(kind='bar', color=['salmon', 'lightskyblue', 'springgreen', 'khaki'])
plt.title('Chest pain type vs count')
plt.show()
print(pd.crosstab(df.sex, df.cp))
pd.crosstab(df.sex, df.cp).plot(kind='bar', color=['coral', 'lightskyblue', 'plum', 'khaki'])
plt.title('Type of chest pain for sex')
plt.xlabel('0 = Female, 1 = Male')
plt.show()
# Most of male has type 0 chest pain and least of male has type 4 pain
# In case of female type 0 and type 2 percentage is almost same.
# --- 4. People with which chest pain are most pron to have heart disease?
print(pd.crosstab(df.cp, df.target))
sns.countplot(x='cp', data=df, hue='target')
plt.show()
# Most of the people have type 0 chest pain has less chance of heart disease.
# Opposite for other case
# Creating distribution plot with normal distribution curve for age column
sns.displot(x='age', data=df, bins=30, kde=True)
plt.show()
# Dataset consist majority of '58-59' year old people. 
# Distrivution plot for maximum heart rate.
sns.displot(x='thalach', data=df, bins=30, kde=True, color='chocolate')
plt.show()
# This plot shows maximum heart rate achieved by 'thalach' column.
# --- 5. Do people with higher blood pressure (trestbps) tend to have higher cholesterol (chol)?
plt.figure(figsize=(8, 6))
plt.scatter(df['trestbps'], df['chol'], c=df['target'], cmap='viridis', alpha=0.7)
plt.xlabel('Resting Blood Pressure (trestbps)')
plt.ylabel('Cholesterol (chol)')
plt.title('Resting Blood Pressure vs Cholesterol (colored by Heart Disease)')
plt.legend(title='Heart Disease', labels=['No (target=0)', 'Yes (target=1)'], loc='upper right')
plt.grid(True)
plt.show()
# This chart shows the relationship between trestbps and chol
# --- 6. Does resting blood pressure are different in different age groups?
plt.bar(df.age, df.trestbps)
plt.xlabel("age")
plt.ylabel("trestbps")
plt.title("Age vs Resting Blood Pressure")
plt.show()
# This chart shows that in 50-60 age group, resting blood pressure shows its fluctuation in its trestbps.
# In 60-70 age group, resting blood pressure gets changed to a higher point when compared to 30-50 age group.
# --- 7. What is the relationship between slop and target?
sns.countplot(data=df, x='slope',hue='target')
plt.title('Slope v/s Target\n')
plt.show()