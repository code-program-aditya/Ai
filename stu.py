import pandas as pd
import matplotlib.pyplot as plt

students_data = {
    'student': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'roll no': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'marks': [78, 85, 92, 67, 74, 88, 95, 71, 82, 89],
    'grade': ['B', 'A', 'A', 'C', 'B', 'A', 'A', 'C', 'B', 'A']
}

df = pd.DataFrame(students_data)
df
df.describe()
print(df.head())
print(df.tail())
print('DataFrame:')
print(df)
print('\nStatistics for marks:')
print('Mean:', df['marks'].mean())
print('Median:', df['marks'].median())
print('Mode:', df['marks'].mode().tolist())
print('Average (mean):', df['marks'].mean())
print('Min:', df['marks'].min())
print('Max:', df['marks'].max())
plt.figure(figsize=(10, 6))
plt.hist(df['marks'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.grid(axis='y', alpha=0.75)
plt.show()
