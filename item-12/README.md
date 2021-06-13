# Item 11 - Don't mix slicing and steps in a single command

```
$ python3 ./
```

- makes for confusing code - rather use 2 statements

  ```python
  xs = list(range(10))

  xs[-2::-1]
  ```
