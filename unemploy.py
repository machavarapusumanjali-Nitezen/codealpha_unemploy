import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# Plot unemployment rate
plt.figure(figsize=(10,5))
plt.plot(df.index, df['Estimated Unemployment Rate (%)'])
plt.title("Estimated Unemployment Rate in India")
plt.xlabel("Records")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()
# Average unemployment rate by region
avg_unemployment = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

plt.figure(figsize=(12,6))
avg_unemployment.sort_values().plot(kind="bar")
plt.title("Average Unemployment Rate by Region")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()


