# Importing pandas library
import pandas as pd
# Reading .csv file with pandas
df = pd.read_csv("/Users/gopalsharma/Documents/Python/MFST/Task_2/dataset.csv")
# Checking the class of dataframe
print(type(df))
# Quick overview of dataframe
print(df.info)
# Checking the descriptive statistics of numeric data in dataframe
print(df.describe)
# Removing duplicate entries
df = df.drop_duplicates()
print(df)
# Identifying missing values in dataframe (Boolean values)
print(df.isnull())
# Identifying missing values in each column of dataframe (True values)
print(df.isnull().sum())
# Identifying the total number of missing values in dataframe
print(df.isnull().sum().sum())
# Identifying valid (non-missing) data in dataframe (Boolean values)
print(df.notnull())
# Identifying valid (non-missing) data in each column of dataframe (True values)
print(df.notnull().sum())
# Identifying the total number of valid (non-missing) data in dataframe
print(df.notnull().sum().sum())
# ---------- Methods of filling missing values in dataframe
# Filling missing values with a specific value
df2 = df.fillna(0)
print(df2)
# Filling missing values with the value from the previous non-null value in the same column - (ffill/pad - forward fill)
# df2 = df.fillna(method='pad')
# print(df2)
# Filling missing values with the value from the previous non-null value in the same column - (bfill - backward fill)
# df2 = df.fillna(method='bfill')
# Retrieve the labels (names) of each column in the dataframe
print(df2.columns)
# Retrieve the index (names) of each row in the dataframe
print(df2.index)
# Permanently removing a column in dataframe
df2.drop(['Observation'], axis=1, inplace=True)
print(df2.columns)
# Calculation of IQR
Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)
IQR = Q3 - Q1
# Identifying outliers (1.5 IQR below Q1 or above Q3)
outlier_mask = ~((df2 < (Q1 - 1.5 * IQR)) | (df2 > (Q3 + 1.5 * IQR))).any(axis=1)
df3 = df2[outlier_mask]
print("Original Data:")
print(df2)
print("\nData After Removing Outliers:")
print(df3)
# Checking the descriptive statistics of numeric data in dataframe
print(df3.describe())
