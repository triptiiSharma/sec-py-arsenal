# create a program that can take in input of the user name
# save the name in the variable
# pass the variable through the function and print "Hello _______________"

name = input("Enter your name: ")

def printName(name):
    print(f"Hello! {name}")

printName(name)