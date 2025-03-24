import pandas as pd
import numpy as np

# Reading csv file
df = pd.read_csv('e1.csv')

# Part.1    Mean and median for Age and Weight
age_mean = df['Age'].mean()
weight_mean = df['Weight'].mean()
print(f"Age Mean = {age_mean}\nWeight Mean = {weight_mean}")
age_median = df['Age'].median()
weight_median = df['Weight'].median()
print(f"Age Median = {age_median}\nWeight Median = {weight_median}")
print(40 * "*")

# Part.2    Mode for Height, Gender, Education (All Modes)
height_mode = [_ for _ in df['Height'].mode()]
gender_mode = [_ for _ in df['Gender'].mode()]
education_mode = [_ for _ in df['Education'].mode()]
print(f"Height Mode = {height_mode}")
print(f"Gender Mode = {gender_mode}")
print(f"Education Mode = {education_mode}")
print(40 * "*")

# Part.3    Data Range for Age, Height, Weight
age_range = np.ptp(df['Age'])
height_range = np.ptp(df['Height'])
weight_range = np.ptp(df['Weight'])
print(f"Age Range = {age_range}")
print(f"Height Range = {height_range}")
print(f"Weight Range = {weight_range}")
print(40 * "*")

# Part.4 Variance and Standard Deviation for Age, Height, Weight
age_var = df['Age'].var()
height_var = df['Height'].var()
weight_var = df['Weight'].var()
print(f"Age Variance = {age_var}")
print(f"Height Variance = {height_var}")
print(f"Weight Variance = {weight_var}")
age_std = df['Age'].std()
height_std = df['Height'].std()
weight_std = df['Weight'].std()
print(f"Age Standard Deviation = {age_std}")
print(f"Height Standard Deviation = {height_std}")
print(f"Weight Standard Deviation = {weight_std}")
print(40 * "*")

# Part.5 Quartiles for Age, Height, Weight
age_quartiles = np.percentile(df['Age'], [25, 50, 75])
height_quartiles = np.percentile(df['Height'], [25, 50, 75])
weight_quartiles = np.percentile(df['Weight'], [25, 50, 75])
print(f"Age Quartiles = {age_quartiles}")
print(f"Height Quartiles = {height_quartiles}")
print(f"Weight Quartiles = {weight_quartiles}")
print(40 * "*")

# Part.6 IQR for Age, Height, Weight
age_iqr = np.percentile(df['Age'], 75) - np.percentile(df['Age'], 25)
height_iqr = np.percentile(df['Height'], 75) - np.percentile(df['Height'], 25)
weight_iqr = np.percentile(df['Weight'], 75) - np.percentile(df['Weight'], 25)
print(f"Age IQR = {age_iqr}")
print(f"Height IQR = {height_iqr}")
print(f"Weight IQR = {weight_iqr}")