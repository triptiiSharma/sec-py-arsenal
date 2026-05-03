# find all the numbers divisible by 3 from 1-100

for num in range(0, 100, 3):
    print(num)

for num in range(1, 100):
    if num % 3 == 0:
        print(num)