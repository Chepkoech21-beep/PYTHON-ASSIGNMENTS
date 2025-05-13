# Task 1: Load and Explore the Dataset

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set plot style
sns.set(style="whitegrid")

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# No missing values in Iris dataset, but if there were:
# df.fillna(method='ffill', inplace=True) or df.dropna(inplace=True)

# Task 2: Basic Data Analysis

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Grouping by species and computing mean
print("\nMean measurements per species:")
print(df.groupby('species').mean())

# Task 3: Data Visualization

# 1. Line chart (mock time series for demo purposes)
# We'll pretend sepal length is measured over time
df_line = df.copy()
df_line['measurement_id'] = df_line.index

plt.figure(figsize=(10, 5))
plt.plot(df_line['measurement_id'], df_line['sepal length (cm)'], label='Sepal Length')
plt.title('Mock Time Series of Sepal Length')
plt.xlabel('Measurement ID')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# 2. Bar chart: Average petal length per species
avg_petal = df.groupby('species')['petal length (cm)'].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=avg_petal, x='species', y='petal length (cm)', palette='viridis')
plt.title('Average Petal Length per Species')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Species')
plt.show()

# 3. Histogram of sepal length
plt.figure(figsize=(8, 5))
plt.hist(df['sepal length (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot: Sepal vs Petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set1')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# Findings/Observations:
print("\nObservations:")
print("- Iris setosa tends to have shorter petal length and sepal length.")
print("- Iris virginica has the longest petals on average.")
print("- Sepal and petal lengths are positively correlated, especially for virginica and versicolor.")
