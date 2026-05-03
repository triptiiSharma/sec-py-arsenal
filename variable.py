x = 5
y = 8
print(x+y)

a = "Tripti"
b = "Sharma"
print(a+b)

# adding a number and string

a = 3
b = "Sharma"
# print(a+b) # it will result in error because we can't add string and integer

a = 3
b = "Sharma"
print(str(a)+b) # this will redefine our a as string now rather than an integer

c = "3"
d = 10
# print(c+d) # this will throw an error
print(int(c)+d) # will convert the string to integer

# Exercise - Take a first name as variable and last name, then print to console "My name is --------------"
fname = input("What is your first name? ")
lname = input("What is your last name? ")
print("My name is " + fname + " " + lname)
print(f"My name is {fname} {lname}")