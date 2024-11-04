# -*- coding: utf-8 -*-
"""Task-6

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w2mi8qXrwMNISl6oxqOQD3tQTGazj-Si
"""

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('/content/heart.csv')

df.head()

"""## 1. Data Cleaning"""

# Check for missing values
missing_values = df.isnull().sum()

# Fill or drop missing values based on context (e.g., using mean imputation for numerical columns)
df.fillna(df.mean(), inplace=True)

# Detect outliers (example: using IQR for a column like 'cholesterol')
Q1 = df['chol'].quantile(0.25)
Q3 = df['chol'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['chol'] < (Q1 - 1.5 * IQR)) | (df['chol'] > (Q3 + 1.5 * IQR)))]

# Ensure correct data types and fix any inconsistencies if needed
df['age'] = df['age'].astype(int)  # Ensure age is an integer

"""## 2. Exploratory Data Analysis (EDA)"""

import seaborn as sns
import matplotlib.pyplot as plt

# Summary statistics
print(df.describe())

# Distribution of key variables
plt.figure(figsize=(8,4))
sns.histplot(df['age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.show()

# Correlation matrix
plt.figure(figsize=(8,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Pairplot to see relationships between multiple variables
plt.figure(figsize=(10,5))
sns.pairplot(df, hue='target')  # Assuming 'target' is the column for heart disease presence
plt.show()

"""## 3. Question Formulation and Solving"""

#Age Distribution of Individuals with Heart Disease

heart_disease_age = df[df['target'] == 1]['age']
plt.figure(figsize=(8,4))
sns.histplot(heart_disease_age, bins=20, kde=True)
plt.title('Age Distribution for Individuals with Heart Disease')
plt.show()

#Cholesterol Level Correlation with Heart Disease
plt.figure(figsize=(8, 4))
sns.boxplot(x='target', y='chol', data=df)
plt.title('Cholesterol Levels by Heart Disease Status')
plt.show()

#Heart Disease Rates by Gender
plt.figure(figsize=(8, 4))
sns.boxplot(x='target', y='trestbps', data=df)
plt.title('Blood Pressure by Heart Disease Status')
plt.show()

#Heart Disease Rates by Gender
gender_counts = df.groupby(['sex', 'target']).size().unstack()
gender_counts.plot(kind='bar', stacked=True)
plt.title('Heart Disease by Gender')
plt.xlabel('Gender (0 = Female, 1 = Male)')
plt.ylabel('Count')
plt.show()

#Risk of Heart Disease by Age Group
age_groups = pd.cut(df['age'], bins=[0, 30, 45, 60, 100], labels=['<30', '30-45', '45-60', '>60'])
age_heart_disease = df.groupby([age_groups, 'target']).size().unstack().fillna(0)
age_heart_disease.plot(kind='bar', stacked=True)
plt.title('Heart Disease by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()

"""## 4. Data Visualization"""

#Cholesterol vs. Heart Disease Status Scatter Plot
plt.figure(figsize=(7,4))
sns.scatterplot(x='chol', y='age', hue='target', data=df, palette='viridis')
plt.title('Cholesterol Levels and Age by Heart Disease Status')
plt.xlabel('Cholesterol')
plt.ylabel('Age')
plt.show()

#Overall Heatmap of Variables
plt.figure(figsize=(9, 5))
sns.heatmap(df.corr(), annot=True, cmap='YlGnBu')
plt.title('Heatmap of Variables')
plt.show()