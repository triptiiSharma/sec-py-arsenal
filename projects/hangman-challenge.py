# create a greeting
# create your word list
# randomly choose the word from the list you have created
# ask the user to guess a letter
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in the word

import random

name = input("Enter your name: ")
print(f"Hello {name}! welcome to this hangman game")

wordList = ["meow", "sherni", "tripti"]

secret_word = random.choice(wordList)

userChoice = input("guess a letter: ").lower()

for letter in secret_word:
    if letter == userChoice:
        print("right!")
    else:
        print("incorrect!")