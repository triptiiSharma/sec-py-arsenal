# Data Types

## What is a Data Type?
A category for values. Every value belongs to exactly one data type.

## Common Data Types

| Data Type | Description | Examples |
|-----------|-------------|----------|
| **Integer (int)** | Whole numbers | `-2, -1, 0, 1, 2, 42` |
| **Float** | Decimal numbers | `-1.25, 0.0, 3.14, 42.0` |
| **String (str)** | Text in quotes | `'a', 'Hello!', '11 cats'` |

## Integers
Whole numbers without decimal points

```python
>>> 42
42
>>> -5
-5
>>> 0
0
```

## Floating-Point Numbers
Numbers with decimal points

```python
>>> 3.14
3.14
>>> 42.0    # Note: 42.0 is a float, 42 is an int
42.0
>>> -0.5
-0.5
```

## Strings
Text values surrounded by single quotes

```python
>>> 'Hello'
'Hello'
>>> 'Goodbye cruel world!'
'Goodbye cruel world!'
>>> ''      # Empty/blank string
''
```

### String Rules
- Must be surrounded by single quotes `'` 
- Forget closing quote → `SyntaxError: EOL while scanning string literal`

```python
>>> 'Hello world!
SyntaxError: EOL while scanning string literal
```

## String Operations

### Concatenation (`+`)
Joins strings together

```python
>>> 'Alice' + 'Bob'
'AliceBob'
```

**Cannot mix strings and numbers:**
```python
>>> 'Alice' + 42
TypeError: Can't convert 'int' object to str implicitly
```

### Replication (`*`)
Repeats strings

```python
>>> 'Alice' * 5
'AliceAliceAliceAliceAlice'
```

**Only works with string * integer:**
```python
>>> 'Alice' * 5      # Valid
>>> 5 * 'Alice'      # Also valid
>>> 'Alice' * 'Bob'  # Invalid
>>> 'Alice' * 5.0    # Invalid (must be int, not float)
```

## Type Equivalence

### Numbers vs Strings
String version of a number ≠ the actual number

```python
>>> 42 == '42'
False            # Different types

>>> 42 == 42.0
True             # Int and float with same value are equal

>>> 42.0 == 0042.000
True
```

## Key Points
- Data type determines what operations are valid
- `+` means addition for numbers, concatenation for strings
- `*` means multiplication for numbers, replication for strings
- Cannot mix string and number operations without conversion
- Strings are always in quotes; numbers are not