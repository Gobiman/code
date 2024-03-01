# Import the random module
import random

# Define the number of lists to generate
m = 3

# Define the number of elements in each list
n = 5

# Create an empty list to store the lists of random numbers
random_lists = []

# Create an empty dictionary to store the numbers that have been generated
generated_numbers = {}

# Use a for loop to generate m lists
for j in range(m):
    # Create an empty set to store the random numbers
    random_set = set()
    # Use another for loop to generate n random numbers
    for i in range(n):
        # Generate a random number between 1 and 50
        num = random.randint(1, 50)
        # Check if the number has been generated before
        if num not in generated_numbers:
            # Add the number to the set
            random_set.add(num)
            # Mark the number as generated in the dictionary
            generated_numbers[num] = True
    # Convert the set to a list and append it to the list of lists
    random_list = list(random_set)
    random_lists.append(random_list)

# Print the list of lists
print(random_lists)
