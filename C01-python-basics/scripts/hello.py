"""
Hello Program
From Chapter 1 - demonstrates variables, input(), and string concatenation
"""

# Ask for user's name
print('Hello world!')
print('What is your name?')
myName = input()

# Greet the user
print('It is good to meet you, ' + myName)

# Ask for user's age
print('What is your age?')
myAge = input()

# Calculate age next year (convert string to int, add 1, convert back to string)
print('You will be ' + str(int(myAge) + 1) + ' in a year.')