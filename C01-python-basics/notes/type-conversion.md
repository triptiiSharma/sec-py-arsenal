# Type Conversion

## Why Type Conversion?
Cannot mix strings and numbers in operations - must convert first

```python
>>> 'I am ' + 29 + ' years old.'
TypeError: Can't convert 'int' object to str implicitly
```

## Conversion Functions

### `str()` - Convert to String

```python
>>> str(29)
'29'

>>> str(0)
'0'

>>> str(-3.14)
'-3.14'
```

**Use case**: Concatenating numbers with strings
```python
>>> print('I am ' + str(29) + ' years old.')
I am 29 years old.
```

### `int()` - Convert to Integer

```python
>>> int('42')
42

>>> int('-99')
-99

>>> int(1.25)      # Rounds DOWN (truncates decimal)
1

>>> int(1.99)
1
```

**Use case**: Converting string input for math
```python
>>> age = input()      # User enters "25"
>>> age
'25'                   # It's a string!

>>> age = int(age)     # Convert to int
>>> age
25                     # Now it's an integer
```

### `float()` - Convert to Float

```python
>>> float('3.14')
3.14

>>> float(10)
10.0
```

## Common Errors

### Invalid Conversions

```python
>>> int('99.99')
ValueError: invalid literal for int() with base 10: '99.99'
# Can't convert decimal string directly to int

>>> int('twelve')
ValueError: invalid literal for int() with base 10: 'twelve'
# Can't convert words to numbers
```

## `input()` Function
**Always returns a string** - even if user types numbers

```python
>>> spam = input()
101                # User types 101

>>> spam
'101'              # Stored as string, not int!

>>> spam * 10
ERROR              # Can't do math on string
```

**Solution**: Convert with `int()` or `float()`
```python
>>> spam = input()
101

>>> spam = int(spam)    # Convert to integer
>>> spam
101                     # Now it's an int

>>> spam * 10
1010                    # Math works!
```

## Chained Conversions
Multiple conversions in one expression

```python
>>> age = input()       # User enters "4"

# Break down what happens:
int(age)               # '4' → 4
int(age) + 1           # 4 + 1 → 5
str(int(age) + 1)      # 5 → '5'

>>> print('You will be ' + str(int(age) + 1) + ' in a year.')
You will be 5 in a year.
```

## `len()` Function
Returns length of a string (as an integer)

```python
>>> len('hello')
5

>>> len('')
0

>>> len('My very energetic monster just scarfed nachos.')
46
```

**Cannot use on numbers:**
```python
>>> len(42)
TypeError: object of type 'int' has no len()
```

## Key Points
- `input()` always returns strings - convert for math
- `int()` truncates decimals (doesn't round)
- Can't convert invalid strings to numbers
- `len()` only works on strings, not numbers
- Use conversion functions to mix types in operations

## Common Patterns

```python
# Get numeric input
age = int(input('Enter age: '))

# Get float input
price = float(input('Enter price: '))

# Concatenate number with string
print('Total: ' + str(total))

# Check string length
if len(password) < 8:
    print('Password too short')
```