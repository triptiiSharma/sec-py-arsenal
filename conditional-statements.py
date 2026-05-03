fnum = input("What is the first number? ")
snum = input("What is the second number? ")

if fnum > snum: 
    print("The first number is bigger.")
elif snum > fnum:
    print("The second number is larger")
else:
    print("Both the numbers are same.")

# nested - if

score = int(input("Enter your score: "))

if score >= 90:
    age = int(input("Enter your age: "))
    if age <= 10:
        print("You have grade A+")
    else:
        print("You have grade A")
elif score >= 80:
    print("You have grade B")
elif score >= 70:
    print("You have grade C")
elif score >= 60:
    print("You have grade D")
else:
    print("You have grade F")