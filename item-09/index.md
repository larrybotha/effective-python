# Item 9 - Avoid `else` blocks after `for` and `while` loops

```
$ python3 main.py
```

- `else` can follow `for` or `while`:

  ```python
  # prints 0 to 10
  for i in range(10):
    print(i)
  else:
    print(10)
  ```
- `else` in `for` and `while` loops will always execute, unless the loop is
  short-circuited with a `break`
- empty iterables will fire the else block, as will `while` loops that first
  evaluate to `False`
- this is surprising behaviour - few, if any, languages have this. Avoid it for
  the sake of readability

