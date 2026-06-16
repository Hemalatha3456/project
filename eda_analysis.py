
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv")

print(df.head())
print(df.describe())

print(df.isnull().sum())

df['Marks'].plot(kind='hist')
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
