# Expressions and Operators

## What is an Expression?
An expression is a combination of values and operators that evaluates to a single value.

```python
2 + 2        # Evaluates to 4
2 + 3 * 6    # Evaluates to 20
(2 + 3) * 6  # Evaluates to 30
```

## Math Operators (Precedence Order)

| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `**` | Exponent | `2 ** 3` | `8` |
| `%` | Modulus (remainder) | `22 % 8` | `6` |
| `//` | Integer division | `22 // 8` | `2` |
| `/` | Division | `22 / 8` | `2.75` |
| `*` | Multiplication | `3 * 5` | `15` |
| `-` | Subtraction | `5 - 2` | `3` |
| `+` | Addition | `2 + 2` | `4` |

## Order of Operations (Precedence)
1. `**` (exponent) - evaluated first
2. `*`, `/`, `//`, `%` - evaluated left to right
3. `+`, `-` - evaluated last, left to right
4. Use parentheses `()` to override precedence

### Examples
```python
>>> 2 + 3 * 6
20                    # Multiplication first: 3*6=18, then 2+18=20

>>> (2 + 3) * 6
30                    # Parentheses first: 2+3=5, then 5*6=30

>>> 2 ** 8
256

>>> 23 / 7
3.2857142857142856    # Regular division (float result)

>>> 23 // 7
3                     # Integer division (no decimal)

>>> 23 % 7
2                     # Remainder
```

## Expression Evaluation
Python evaluates expressions step by step until a single value remains:

```
(5 - 1) * ((7 + 1) / (3 - 1))
    4  * ((7 + 1) / (3 - 1))
    4  * (   8    / (3 - 1))
    4  * (   8    /    2   )
    4  * 4.0
    16.0
```

## Syntax Errors
Invalid expressions cause `SyntaxError`:

```python
>>> 5 +
SyntaxError: invalid syntax

>>> 42 + 5 + * 2
SyntaxError: invalid syntax
```

## Key Points
- Expressions always reduce to a single value
- A value by itself is also an expression (`2` evaluates to `2`)
- Follow standard mathematical precedence rules
- Use parentheses to control evaluation order
- Syntax errors won't break your computer - they just stop the program