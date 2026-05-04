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
# create an empty list 
# for each item in the secret_word add a "_" that will be printed to the console 
# example if the word is hacker - "_", "_", "_", "_", "_", "_"

secret_word = random.choice(wordList)
display_word = []

for letter in secret_word:
    display_word += "_"

print(display_word)

# loop through each of the letters in the chosen word 
# if the letter is in the word replace the "_" with the letter 
# it should look like this - "_", "_", "c", "_", "_", "r"

game_over = False

while not game_over:

    userChoice = input("guess a letter: ").lower()

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == userChoice:
            display_word[position] = letter 

    print(display_word)

    if "_" not in display_word:
        print("You win!")
        game_over = True 