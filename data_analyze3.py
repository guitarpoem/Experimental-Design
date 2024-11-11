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

# Convert necessary columns to numeric for calculations
df['correctCount'] = pd.to_numeric(df['correctCount'])

# Group by 'userColor' and 'correctCount', then count the occurrences
color_correct_distribution = df.groupby(['userColor', 'correctCount']).size().unstack(fill_value=0)

# Display the distribution
print("Distribution of Correct Count Based on User Color:")
print(color_correct_distribution)


# Separate black and non-black colors
black_correct_total = df[df['userColor'] == 'black']['correctCount'].sum()
non_black_correct_total = df[df['userColor'] != 'black']['correctCount'].sum()

# Print the results
print(f"Total Correct Count for 'black' color: {black_correct_total}")
print(f"Total Correct Count for all other colors combined: {non_black_correct_total}")

# Comparison
if black_correct_total > non_black_correct_total:
    print("Users with 'black' color have a higher total correct count.")
elif black_correct_total < non_black_correct_total:
    print("Users with colors other than 'black' have a higher total correct count.")
else:
    print("Total correct counts for 'black' and all other colors are equal.")
    
    
    # Group by 'userColor' and 'correctCount', then count the occurrences
color_correct_distribution = df.groupby(['userColor', 'correctCount']).size().unstack(fill_value=0)

# Separate the distribution for 'black' color
black_distribution = color_correct_distribution.loc['black']

# Sum up the distributions of all other colors
other_colors_distribution = color_correct_distribution.drop('black', axis=0).sum()

# Combine into a new DataFrame for comparison
comparison_df = pd.DataFrame({
    'Black': black_distribution,
    'Other Colors': other_colors_distribution
})

# Plot the comparison as a bar chart
comparison_df.plot(kind='bar', figsize=(12, 8))

# Adding title and labels
plt.title('Comparison of Correct Count Distribution: Black vs Other Colors')
plt.xlabel('Correct Count')
plt.ylabel('Number of Users')
plt.legend(title='Color Group')
plt.tight_layout()

plt.show()