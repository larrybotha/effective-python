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
- Python doesn't have a switch statement, but the walrus operator can be used to
  similar effect:

  ```python
  some_dict = {
    'a': randint(0, 10),
    'b': randint(0, 10),
    'c': randint(0, 10)
  }

  if (value := some_dict.get('a', 0)) > 0:
    print(f'we got a at  {value}')
  elif (value := some_dict.get('b', 0)) > 0:
    print(f'we got b at  {value}')
  elif (value := some_dict.get('c', 0)) > 0:
    print(f'we got c at  {value}')
  else:
    print('default')
  ```
- Python has no `do / while` loop. This can be overcome with a loop-and-a-half -
  a `while` loop that always evaluate to `True`, but contains a `break`:

  ```python
  while True:
    # do something
    # ...

    if some_condition:
      break
  ```

  This can be improved using an expression assignment:

  ```python
  while (some_value := True):
    # do something
    # ...

    if some_condition:
      some_value = False
  ```
