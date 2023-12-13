import pandas as pd
import matplotlib.pyplot as plt

# Load the Bank Marketing dataset
excel_url = r"C:\Users\karan\Downloads\API_SP.POP.TOTL_DS2_en_excel_v2_6224757.xls"
df = pd.read_excel(excel_url)
print(df.columns)
# Assuming 'Age' is the actual column name, replace it accordingly
age_column = 'Unnamed: 5'  # Update this with the correct column name

# Plot a histogram for the 'Age' variable
plt.figure(figsize=(10, 6))
plt.hist(df[age_column], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'Unnamed: 2' is the job column and 'Unnamed: 4' is the age column, update these with the correct column names
job_column = 'Unnamed: 2'
age_column = 'Unnamed: 4'

# Select the 'job' column as the categorical variable
job_distribution = df[job_column].value_counts()

# Plot a bar chart
plt.figure(figsize=(10, 6))
job_distribution.plot(kind='bar', color='skyblue')
plt.title('Distribution of Job Types')
plt.xlabel('Job Types')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()

# Plot a histogram for the 'age' variable
plt.figure(figsize=(10, 6))
plt.hist(df[age_column].dropna(), bins=20, color='skyblue', edgecolor='black')  # Drop NaN values in the 'age' column
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
plt.close('all')




