# -*- coding: utf-8 -*-
"""task-5.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eXFTKfQ9SsvIFHep7LwoPuOFxNev5J31
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/heart.csv')
df.head()

missing_val = df.isnull().sum()
missing_val

# Identify and handle outliers (example: using z-score)
from scipy import stats
df = df[(np.abs(stats.zscore(df.select_dtypes(include='number'))) < 3).all(axis=1)]
df.head()

df.describe()

# Histograms
df.hist(bins=15, figsize=(15, 10))
plt.show()

# Correlation matrix
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

#1. What is the average age of patients with heart disease?
average_age = df[df['target'] == 1]['age'].mean()
print("Average age of patients with heart disease:", average_age)

#2. Is there a correlation between cholesterol levels and the presence of heart disease?
cholesterol_corr = df['chol'].corr(df['target'])
print("Correlation between cholesterol levels and heart disease:", cholesterol_corr)

#3. What percentage of patients has high blood pressure?
high_blood_pressure_percentage = (df['trestbps'] > 140).mean() * 100
print("Percentage of patients with high blood pressure:", high_blood_pressure_percentage)

#4. How does age affect the likelihood of heart disease?
age_bins = [29, 39, 49, 59, 69, 79]
age_labels = ['30-39', '40-49', '50-59', '60-69', '70-79']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

age_effect = df.groupby('age_group')['target'].mean()
print("Likelihood of heart disease by age group:\n", age_effect)

#5. What is the distribution of heart disease among different age groups?

age_distribution = df['age_group'].value_counts(normalize=True) * 100
print("Distribution of heart disease among age groups:\n", age_distribution)

#6. Is there a gender difference in heart disease prevalence?
gender_distribution = df.groupby('sex')['target'].mean() * 100
print("Heart disease prevalence by gender:\n", gender_distribution)

#7. What is the relationship between physical activity and heart disease?
activity_corr = df['thalach'].corr(df['target'])
print("Correlation between physical activity and heart disease:", activity_corr)

# 1. Average age of patients with heart disease
plt.figure(figsize=(8, 5))
sns.histplot(df[df['target'] == 1]['age'], bins=20, kde=True)
plt.title('Age Distribution of Patients with Heart Disease')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 2. Cholesterol levels vs. heart disease
plt.figure(figsize=(8, 5))
sns.boxplot(x='target', y='chol', data=df)
plt.title('Cholesterol Levels by Heart Disease Presence')
plt.xlabel('Heart Disease (0 = No, 1 = Yes)')
plt.ylabel('Cholesterol Level')
plt.show()

# 3. Heart disease prevalence by gender
plt.figure(figsize=(8, 5))
sns.barplot(x=gender_distribution.index, y=gender_distribution.values)
plt.title('Heart Disease Prevalence by Gender')
plt.xlabel('Gender')
plt.ylabel('Prevalence (%)')
plt.show()