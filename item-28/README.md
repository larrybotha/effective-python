# Item 28 - Avoid nesting list comprehensions more than 2 levels

```shell
$ python3 ./
```

- comprehensions can be nested:

  ```python
  xxs = [[1,2,3], [4,5,6]]
  xs = [x for row in xxs for x in row]

  # [1,2,3,4,5,6]
  ```
- nesting comprehensions is already tricky to read at 2 levels of nesting, avoid
  any further nesting
