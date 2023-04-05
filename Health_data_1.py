import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('health_data.csv')

# Data preprocessing
df['date'] = pd.to_datetime(df['date'])
df['age'] = df['age'].astype(int)
df.dropna(subset=['weight', 'height'], inplace=True)

# Feature engineering
df['bmi'] = df['weight'] / (df['height'] / 100) ** 2
df['risk'] = np.where(df['bmi'] >= 25, 'High', 'Low')

# Data visualization
sns.histplot(data=df, x='bmi', hue='risk', kde=True, alpha=0.7)
plt.title('Distribution of BMI by Risk Level')
plt.xlabel('BMI')
plt.ylabel('Count')
plt.show()

# Data analysis
avg_bmi = df['bmi'].mean()
std_bmi = df['bmi'].std()
max_bmi = df['bmi'].max()

print(f'Average BMI: {avg_bmi:.2f}')
print(f'Standard deviation of BMI: {std_bmi:.2f}')
print(f'Maximum BMI: {max_bmi:.2f}')
