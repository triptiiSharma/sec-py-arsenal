"""
String Operations Examples
Demonstrates string concatenation and replication
"""

# String concatenation (+)
print("=== String Concatenation ===")
print("'Alice' + 'Bob' =", 'Alice' + 'Bob')
print("'Hello' + ' ' + 'world!' =", 'Hello' + ' ' + 'world!')

# String replication (*)
print("\n=== String Replication ===")
print("'Alice' * 5 =", 'Alice' * 5)
print("'Python' * 3 =", 'Python' * 3)
print("'-' * 20 =", '-' * 20)

# Mixing operations
print("\n=== Mixed String Operations ===")
greeting = 'Hello' + ' ' + 'Python'
print("greeting =", greeting)

separator = '=' * 30
print(separator)

# String length
print("\n=== String Length ===")
print("len('hello') =", len('hello'))
print("len('') =", len(''))  # Empty string
print("len('Python programming') =", len('Python programming'))

# Common patterns
print("\n=== Common Patterns ===")
border = '*' * 40
title = 'Python Basics'
print(border)
print('*' + ' ' * 38 + '*')
print('*' + title.center(38) + '*')
print('*' + ' ' * 38 + '*')
print(border)