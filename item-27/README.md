# Item 27 - Prefer comprehensions over `map` and `filter`

```shell
$ python3 ./
```

- comprehensions can be easier to read than `map` and `filter` in a few ways:
  - no need to define a lambda (visually noisy)
  - guards are easier to define than nesting `filter` with a lambda
- dictionaries and sets have their own comprehensions, too
