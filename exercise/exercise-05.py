# fizzbuzz challenge

# if a number is divisible by 3, print fizz
# if a number is divisible by 5, print buzz
# if a number is divisible by both, print fizzbuzz


for num in range(0,100):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} : fizzbuzz")
    elif num % 3 == 0:
        print(f"{num} : fizz")
    elif num % 5 == 0:
        print(f"{num} : buzz")
    else:
        print(num)