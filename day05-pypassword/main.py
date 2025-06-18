import random

# List of possible letters (uppercase and lowercase)
letters = [
    'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 
    'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 
    'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 
    'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z'
]

# List of possible digits
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of possible special symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', 
    '\\', '|', '`', '~'
]

print("Welcome to the PyPassword Generator!")

# Ask the user for the number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create an empty list to store the characters of the password
password = []

# Add a random letter for each requested letter
for char in range(nr_letters):
    password.append(random.choice(letters))

# Add a random symbol for each requested symbol
for char in range(nr_symbols):
    password.append(random.choice(symbols))

# Add a random number for each requested number
for char in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the list to ensure the characters are in a random order
random.shuffle(password)

# Join the list into a single string to create the final password
new_password = "".join(password)

# Print the generated password
print(new_password)