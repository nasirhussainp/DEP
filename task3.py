import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Explore the dataset
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Visualize the data
plt.figure(figsize=(8, 5))
df['Pclass'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Number of Passengers by Class')
plt.xlabel('Class')
plt.ylabel('Number of Passengers')
plt.show()
