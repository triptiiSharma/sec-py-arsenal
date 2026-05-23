"""
Password Checker Example
From Chapter 0: Introduction

This is the example code shown in the chapter to demonstrate
basic programming concepts like file I/O, conditionals, and
user input.

NOTE: This is for learning purposes only. In real applications,
never store passwords in plain text files!
"""

# Open the password file and read the secret password
passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()

# Prompt user to enter password
print('Enter your password.')
typedPassword = input()

# Compare entered password with secret password
if typedPassword == secretPassword:
    print('Access granted')
    
    # Extra check for weak password
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')