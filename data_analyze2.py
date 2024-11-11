import json
import pandas as pd

# Load the JSON data from a file
with open('data2.json', 'r') as file:
    data = json.load(file)

# Extract the user data from the nested JSON structure
users_data = [entry['userData'] for entry in data['testData'].values()]

# Convert to a DataFrame for easier analysis
df = pd.DataFrame(users_data)

# Convert age and counts to numeric for calculations
df['age'] = pd.to_numeric(df['age'])
df['correctCount'] = pd.to_numeric(df['correctCount'])
df['incorrectCount'] = pd.to_numeric(df['incorrectCount'])

# Get a summary of key statistics for numerical columns
statistics_summary = df[['age', 'correctCount', 'incorrectCount']].describe()

print("Statistical Summary of the Data:")
print(statistics_summary)
