# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
# Importing dataset csv file
df = pd.read_csv("/Users/gopalsharma/Documents/Python/MFST/Task_3/householdtask3.csv")
# Printing top 10 rows of dataset
print(df.head(10))
# Data visualization with Matplotlib
# --Scatter Plot
# Scatter plot with year against own
plt.scatter(df.year,df.own)
# Adding title to the plot
plt.title('Scatter Plot')
# Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
# Adding color bar to the plot
plt.colorbar()
print(plt.show())
# --Line Chart
# Line chart with year against own
plt.plot(df.year)
plt.plot(df.own)
# Adding title to the plot
plt.title('Line Chart')
# Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
print(plt.show())
# --Bar Chart
# Bar chart with year against own
plt.bar(df.year,df.own)
# Adding title to the plot
plt.title('Bar Chart')
# Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
print(plt.show())
# --Histogram
# Histogram chart with income
plt.hist(df.income)
# Adding title to the plot
plt.title('Histogram')
print(plt.show())