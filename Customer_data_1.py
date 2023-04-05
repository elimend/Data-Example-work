import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("customer_data.csv")

# Data preprocessing
df["date"] = pd.to_datetime(df["date"])
df["age"] = df["age"].astype(int)
df.dropna(subset=["gender", "income"], inplace=True)

# Feature engineering
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 25, 35, 50, 65, 100],
                         labels=["0-18", "19-25", "26-35", "36-50", "51-65", "66+"])
df["age_income"] = pd.cut(df["income"], bins=[0, 30000, 50000, 75000, 100000, 150000, 1000000],
                           labels=["0-30k", "30k-50k", "50k-75k", "75k-100k", "100k-150k", "150k+"])

# Data visualization
plt.figure(figsize=(10, 6))
sns.countplot(x="age_group", hue="gender", data=df)
plt.title("Customer Age Groups by Gender")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.legend(title="Gender")

plt.figure(figsize=(10, 6))
sns.boxplot(x="age_income", y="balance", data=df)
plt.title("Distribution of Account Balances by Age and Income")
plt.xlabel("Age-Income Group")
plt.ylabel("Account Balance ($)")

# Data analysis
num_customers = len(df)
num_males = len(df[df["gender"] == "Male"])
num_females = len(df[df["gender"] == "Female"])
num_transactions = df["transactions"].sum()
avg_balance = df["balance"].mean()
std_balance = df["balance"].std()

print("Number of customers:", num_customers)
print("Number of male customers:", num_males)
print("Number of female customers:", num_females)
print("Total number of transactions:", num_transactions)
print("Average account balance:", round(avg_balance, 2))
print("Standard deviation of account balance:", round(std_balance, 2))
