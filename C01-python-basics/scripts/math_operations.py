"""
Math Operations Examples
Demonstrates Python math operators and order of operations
"""

# Basic arithmetic
print("=== Basic Arithmetic ===")
print("2 + 2 =", 2 + 2)
print("5 - 2 =", 5 - 2)
print("3 * 5 =", 3 * 5)
print("22 / 8 =", 22 / 8)

# Integer division and modulus
print("\n=== Integer Division & Modulus ===")
print("22 // 8 =", 22 // 8)  # Integer division (quotient)
print("22 % 8 =", 22 % 8)    # Modulus (remainder)

# Exponent
print("\n=== Exponent ===")
print("2 ** 3 =", 2 ** 3)
print("2 ** 8 =", 2 ** 8)

# Order of operations (precedence)
print("\n=== Order of Operations ===")
print("2 + 3 * 6 =", 2 + 3 * 6)        # Multiplication first
print("(2 + 3) * 6 =", (2 + 3) * 6)    # Parentheses first

# Complex expression
print("\n=== Complex Expression ===")
result = (5 - 1) * ((7 + 1) / (3 - 1))
print("(5 - 1) * ((7 + 1) / (3 - 1)) =", result)

# Large numbers
print("\n=== Large Numbers ===")
print("48565878 * 578453 =", 48565878 * 578453)