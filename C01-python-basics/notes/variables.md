# Variables

## What is a Variable?
A variable stores a value for later use. Like a box with a label that holds data.

## Assignment Statement
Use `=` to assign a value to a variable

```python
>>> spam = 42
>>> spam
42

>>> eggs = 2
>>> eggs
2
```

## Using Variables in Expressions
Variables can be used anywhere a value can be used

```python
>>> spam = 40
>>> eggs = 2
>>> spam + eggs
42

>>> spam + spam
80

>>> spam = spam + 2    # Take current value, add 2, store back
>>> spam
42
```

## Variable Naming Rules

### Valid Names
- Must start with letter (a-z, A-Z) or underscore (`_`)
- Can contain letters, numbers, underscores
- Case-sensitive (`spam` ≠ `Spam` ≠ `SPAM`)

```python
# Valid variable names
spam
eggs
spam23
_spam
SPAM
Spam
```

### Invalid Names
```python
23spam      # Cannot start with number
spam eggs   # No spaces allowed
spam-eggs   # No hyphens (use underscore instead)
```

### Best Practices
- Use descriptive names: `user_age` instead of `x`
- Use lowercase with underscores: `my_variable`
- Avoid single letters except in loops/short examples

## Variables vs Strings

```python
spam       # Variable (no quotes) - references stored value
'spam'     # String (has quotes) - literal text "spam"
```

### Example
```python
>>> spam = 42
>>> spam          # Variable - returns 42
42
>>> 'spam'        # String - returns the text 'spam'
'spam'
```

## Overwriting Variables
Assignment replaces the previous value

```python
>>> spam = 42
>>> spam
42

>>> spam = 'Hello'    # Changed from int to string
>>> spam
'Hello'

>>> spam = spam + ' world!'
>>> spam
'Hello world!'
```

## Key Points
- Variables store values for reuse
- `=` is assignment (not equality check)
- Variable names are case-sensitive
- Variables can change type (from int to string, etc.)
- Use descriptive names for readability
- Variable without quotes; string with quotes