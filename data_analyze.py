import json
import pandas as pd
import matplotlib.pyplot as plt

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

# Finding the highest recall count
highest_recall_count = df['correctCount'].max()
print(f"The highest recall count is: {highest_recall_count}")

# Count the number of people at each recall count level
recall_count_distribution = df['correctCount'].value_counts().sort_index()

# Print the number of people at each recall count level
print("Number of People at Each Recall Count Level:")
print(recall_count_distribution)

# Plotting the distribution
plt.figure(figsize=(10, 6))
plt.bar(recall_count_distribution.index, recall_count_distribution.values)
plt.xlabel('Correct Recall Count')
plt.ylabel('Number of People')
plt.title('Distribution of Correct Recall Count')
plt.xticks(recall_count_distribution.index)  # Ensure each recall count is labeled on the x-axis
plt.show()
