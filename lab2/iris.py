import matplotlib
matplotlib.use('Agg')  

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.datasets import load_iris


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

df.iloc[5:10, 1] = np.nan   

print("Original Data (with missing values):")
print(df.head(10))


imputer = SimpleImputer(strategy='mean')
df.iloc[:, :-1] = imputer.fit_transform(df.iloc[:, :-1])

print("\nAfter handling missing values:")
print(df.head(10))


encoder = LabelEncoder()
df['species'] = encoder.fit_transform(df['species'])

print("\nAfter encoding categorical data:")
print(df.head())


scaler = StandardScaler()
df_scaled = df.copy()
df_scaled.iloc[:, :-1] = scaler.fit_transform(df_scaled.iloc[:, :-1])

print("\nAfter feature scaling:")
print(df_scaled.head())


plt.figure(figsize=(6,4))
plt.hist(df['sepal length (cm)'], bins=5, color='pink', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.close()


plt.figure(figsize=(6,4))
sns.scatterplot(x=df['sepal length (cm)'],
                y=df['petal length (cm)'],
                hue=df['species'],
                palette='viridis')
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.savefig("scatter.png")
plt.close()


plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

print("\nPlots saved as:")
print(" - histogram.png")
print(" - scatter.png")
print(" - heatmap.png")

