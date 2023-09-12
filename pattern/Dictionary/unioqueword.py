# Take input from the user
user_input = input("Enter a string: ")

# Initialize an empty list to store unique characters
unique_chars = []

# Iterate over each character in the input string
for char in user_input:
    # Check if the character is not already in the unique_chars list
    if char not in unique_chars:
        # If not, add it to the list
        unique_chars.append(char)

# Count the number of unique characters
count = len(unique_chars)

# Print the count
print("Number of unique characters:", count)
