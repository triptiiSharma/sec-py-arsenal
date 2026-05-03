# printing hello world

print('Hello World') # anything inside the double quotes or single quotes is considered as string. here the line "hello world" is a string.

# newline print

print('Hello world 1 \nHello world 2')
print('Hello world 3')
print('Hello world 4')

# concactenation

print('Tripti' + ' ' + 'Sharma')
print('Tripti' + ' Sharma')

# variables - used to store information

x = "Tripti"
y = "Sharma"
print(x) # Note: do not put quotes around while printing variable else it'll be considered as string and not a variable
print (x + " " + y)
print(f"{x} {y}") # f string is an efficient an concise way to embed variables and expression directly into strings.

# input function

input("What is the target ip? ")

# storing and displaying input

ip = input("What is the target ip? ")
print("Your target ip is: " + ip)

# another way without using variable
print("you are targeting the ip: " + input("What is you target ip? "))