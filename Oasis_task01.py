
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Datasets
df1 = pd.read_csv(r"C:\Users\USER\Downloads\archive (9)\Unemployment in India.csv")
df2 = pd.read_csv(r"C:\Users\USER\Downloads\archive (9)\Unemployment_Rate_upto_11_2020.csv")

#Strip column names for consistency
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

#Display basic info
print("First Dataset:\n", df1.head(), "\n")
print("Second Dataset:\n", df2.head(), "\n")

#Convert 'Date' column to datetime in df2
df2['Date'] = pd.to_datetime(df2['Date'], errors='coerce')

#  Check for null values
print("Missing values in df1:\n", df1.isnull().sum(), "\n")
print("Missing values in df2:\n", df2.isnull().sum(), "\n")

#  Summary statistics
print("Summary of Unemployment Rates (df1):\n", df1['Estimated Unemployment Rate (%)'].describe())
print("\nSummary of Unemployment Rates (df2):\n", df2['Estimated Unemployment Rate (%)'].describe())

#Visualization 1: Unemployment Rate by Region (df1)
plt.figure(figsize=(12, 6))
sns.barplot(data=df1, x='Region', y='Estimated Unemployment Rate (%)', hue='Region', palette='viridis', legend=False)
plt.title('Unemployment Rate by Region')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# Visualization 2: Unemployment Trend Over Time by Region (df2)
plt.figure(figsize=(14, 7))
sns.lineplot(data=df2, x='Date', y='Estimated Unemployment Rate (%)', hue='Region', marker='o')
plt.title('Unemployment Trend Over Time by Region')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#Visualization 3: Heatmap of Unemployment Rate by State and Date (df2)
pivot_data = df2.pivot_table(values='Estimated Unemployment Rate (%)', index='Region', columns='Date')
plt.figure(figsize=(14, 10))
sns.heatmap(pivot_data, cmap="YlGnBu", linecolor='white', linewidths=0.1)
plt.title('Unemployment Rate Heatmap by Region and Date')
plt.tight_layout()
plt.show()

#Save cleaned data if needed
df1.to_csv("Cleaned_Unemployment_in_India.csv", index=False)
df2.to_csv("Cleaned_Unemployment_Rate.csv", index=False)
