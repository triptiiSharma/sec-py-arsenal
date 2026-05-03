# create a greeeting for your program

# ask for the user for the name of the pet

# ask for the name of the city you were born in

# combine the pet name with the word cyber as a new twitter handle and then add the city they are from. 

# the output should look like this "Your new twitter handle and bio @cyberfred from honolulu"

print("Welcome to my program")

name = input("Please enter your name: ")
print(f"Hello {name}!")

petName = input("Enter the name of your pet: ")
city = input("Enter the city you were born in: ")

print(f"Your new twitter handle and bio @cyber{petName} from {city}.")