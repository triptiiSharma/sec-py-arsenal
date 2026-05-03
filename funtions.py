# defining the function

def function():
    print("Hello")

# calling the function

function()

# passing values to the function

choice = int(input("Enter your choice: "))

def fizzbuzz(choice):
    for num in range(0, choice):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num} : fizzbuzz")
        elif num % 3 == 0:
            print(f"{num} : fizz")
        elif num % 5 == 0:
            print(f"{num} : buzz")
        else:
            print(num)

fizzbuzz(choice)