import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('csv_data/budapest_data.csv')
# print(df.head())

# Example: Line plot of temperature over time
df.plot(x='year', y='temperature', kind='line')
plt.show()

