# write a program that prompts the user to enter their score (out of 100) and displays their corresponding grade based on the following criteria:

# scores 90 and above - grade A
# scores 80 to 89 - grade B
# scores 70 to 79 - grade C
# scores 60 to 69 - grade D
# scores below 60 - grade F

score = int(input("Enter your score: "))

if score >= 90:
    print("You have grade A")
elif score >= 80:
    print("You have grade B")
elif score >= 70:
    print("You have grade C")
elif score >= 60:
    print("You have grade D")
else:
    print("You have grade F")