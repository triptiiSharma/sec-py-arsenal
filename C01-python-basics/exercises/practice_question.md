# Chapter 1 Practice Questions

## Questions

1. Which of the following are operators, and which are values?
   - `*`
   - `'hello'`
   - `-88.8`
   - `-`
   - `/`
   - `+`
   - `5`

2. Which of the following is a variable, and which is a string?
   - `spam`
   - `'spam'`

3. Name three data types.

4. What is an expression made up of? What do all expressions do?

5. This chapter introduced assignment statements, like `spam = 10`. What is the difference between an expression and a statement?

6. What does the variable `bacon` contain after the following code runs?
   ```python
   bacon = 20
   bacon + 1
   ```

7. What should the following two expressions evaluate to?
   ```python
   'spam' + 'spamspam'
   'spam' * 3
   ```

8. Why is `eggs` a valid variable name while `100` is invalid?

9. What three functions can be used to get the integer, floating-point number, or string version of a value?

10. Why does this expression cause an error? How can you fix it?
    ```python
    'I have eaten ' + 99 + ' burritos.'
    ```

<br>

## Answers

<details>
<summary>Click to reveal answers</summary>

1. **Operators:** `*`, `-`, `/`, `+`  
   **Values:** `'hello'`, `-88.8`, `5`

2. **Variable:** `spam` (no quotes)  
   **String:** `'spam'` (has quotes)

3. Integer (int), Floating-point (float), String (str)

4. Expressions are made up of values and operators. All expressions evaluate down to a single value.

5. An expression evaluates to a value (e.g., `2 + 2`). A statement is an instruction that performs an action but doesn't necessarily evaluate to a value (e.g., `spam = 10`).

6. `20` - The variable `bacon` contains `20` because `bacon + 1` evaluates to `21` but doesn't assign it back to `bacon`.

7. ```python
   'spam' + 'spamspam'  # Evaluates to 'spamspamspam'
   'spam' * 3           # Evaluates to 'spamspamspam'
   ```

8. Variable names cannot start with a number. They must start with a letter or underscore.

9. `str()`, `int()`, `float()`

10. **Error:** Cannot concatenate string and integer directly.  
    **Fix:** Convert the integer to a string:
    ```python
    'I have eaten ' + str(99) + ' burritos.'
    ```

</details>

<br>

## Extra Credit

Search online for the Python documentation for the `len()` function. It will be on a web page titled "Built-in Functions."

- Skim the list of other functions Python has
- Look up what the `round()` function does
- Experiment with it in the interactive shell

### Example
```python
>>> round(3.14159, 2)
3.14
>>> round(2.7)
3
```