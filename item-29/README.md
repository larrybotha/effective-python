# Item 29 - Assignment expressions in comprehensions to avoid repetition

```shell
$ python3 ./
```

- `//` in Python is for floor division - dividing 2 numbers, and applying
  `floor` to the outcome:

  ```python
  18 // 4
  # => 4
  ```
- an assignment expression can be used to avoid repetition of expression in
  comprehensions.

  ```python
  xs = range(10)
  d = random.randint(0,10)

  # expensive computation is evaluated twice for the same outcome
  ys = [expensive_computation(x) for x in xs if expensive_computation(x) > z]

  # instead, use assignment expression
  ys = [
    ex for x in xs
    if (ex := expensive_computation(x)) and  ex > z
  ]
  ```
- assignment expression can be used in the value part of the expression, it'll
  leak values to the containing scope:

  ```python
  xs = [1, 2, 3]
  ys = [(x := v) for v in xs]

  print(x)
  # => 3 - i.e. leaked
  ```

  - avoid assigning at the value part of the comprehension - only assign in a
    condition, or use a separate comprehension to perform the computation
- `for` loops like the last value, too:

  ```python
  for x in [1,2,3]:
    print(x)

  # 1
  # 2
  # 3

  print(x)
  # 3
  ```
- a _generator expression_ is the name given to what one may think is a tuple
  comprehension - it uses parens, and values are obtained used `next`:

  ```python
  my_gen = ((x, x_squared) for x in [1,2,3] if (x_squared := x**2))

  next(my_gen)
  # (1, 1)

  next(my_gen)
  # (2, 4)

  next(my_gen)
  # (3, 9)
  ```

## Questions

- how does one handle assignment expressions that evaluate to `False`?
