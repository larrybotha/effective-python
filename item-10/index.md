# Item 10 - Use assignment expressions

```
$ python3 ./
```

- an assignment expression is also called the _walrus operator_: `:=`
- `x := y` is pronounced `x walrus y`
- it allows for inline assignment of values:

  ```python
  # if statement
  if (count := get_some_value()) > 0:
    # do some stuff

  while (some_value := get_initial_value()):
    # do some stuff

  for
  ```
