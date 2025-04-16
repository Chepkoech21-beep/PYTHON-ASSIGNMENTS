# 📦 Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1. NumPy: Create an array and calculate the mean
numbers = np.arange(1, 11)  # Array from 1 to 10
mean_value = np.mean(numbers)
print("NumPy Array:", numbers)
print("Mean of numbers:", mean_value)

#  2. pandas: Load a small dataset and show summary statistics
# We'll create a small sample dataset manually
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [88, 95, 79]
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

# 3. requests: Fetch data from a public API
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    btc_data = response.json()
    usd_price = btc_data['bpi']['USD']['rate']
    print(f"\n📈 Current Bitcoin Price in USD: ${usd_price}")
else:
    print("Failed to fetch Bitcoin data")

#  4. matplotlib: Plot a simple line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()
