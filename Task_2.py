import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style='whitegrid')

# Load the dataset
file_path = r"C:\Users\HP\Downloads\gender_submission.csv"
df = pd.read_csv(file_path)

# Display basic information
print(" Shape of dataset:", df.shape)
print("\n Columns:\n", df.columns)
print("\n First 5 rows:\n", df.head())
print("\n Data types:\n", df.dtypes)
print("\n Missing values:\n", df.isnull().sum())
print("\n Summary statistics:\n", df.describe())

# Distribution of target variable: Survived
print("\n Survival distribution:\n", df['Survived'].value_counts())

# Plot survival distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived')
plt.title('Survival Distribution')
plt.xlabel('Survived (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.xticks([0, 1], ['Did not survive', 'Survived'])
plt.tight_layout()
plt.show()
