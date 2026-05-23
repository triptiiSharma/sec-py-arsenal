"""
Type Conversion Examples
Demonstrates str(), int(), float() functions
"""

# str() - Convert to string
print("=== str() - Convert to String ===")
print("str(29) =", str(29))
print("str(0) =", str(0))
print("str(-3.14) =", str(-3.14))

# Using str() for concatenation
age = 29
print("\nConcatenation with str():")
print("'I am ' + str(29) + ' years old.' =", 'I am ' + str(age) + ' years old.')

# int() - Convert to integer
print("\n=== int() - Convert to Integer ===")
print("int('42') =", int('42'))
print("int('-99') =", int('-99'))
print("int(1.25) =", int(1.25))    # Truncates decimal
print("int(1.99) =", int(1.99))    # Rounds DOWN

# float() - Convert to float
print("\n=== float() - Convert to Float ===")
print("float('3.14') =", float('3.14'))
print("float(10) =", float(10))

# input() always returns string
print("\n=== input() Returns String ===")
print("Demonstrating that input() returns a string...")
user_input = input("Enter a number: ")
print("Type of input:", type(user_input))
print("Input value:", user_input)

# Convert input to int for math
num = int(user_input)
print("\nAfter int() conversion:")
print("Type:", type(num))
print("num * 10 =", num * 10)

# Chained conversions
print("\n=== Chained Conversions ===")
text_num = "25"
result = str(int(text_num) + 5)
print("str(int('25') + 5) =", result)

# Type comparison
print("\n=== Type Equivalence ===")
print("42 == '42':", 42 == '42')        # False - different types
print("42 == 42.0:", 42 == 42.0)        # True - same value
print("42.0 == 0042.000:", 42.0 == 0042.000)  # True