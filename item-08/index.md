# Item 8 - Use `zip` to process iterators in parallel

```
$ python3 main.py
```

- multiple iterables can be processed using `zip`:

  ```python
  fruits = ['apple', 'pear', 'naartjie']
  lengths = [len(fruit) for fruit in fruits]

  for fruit, length in zip(fruits, lengths):
    print(f'{fruit} has {length} characters')
  ```
- similar to `enumerate`, `zip` creates a generator from the inputs
- as in Haskell, if the length of the iterators do not match, any items beyond
  the length of the shortest list are ommitted from the generator
- as in Haskell, `zip` consumes list items one at a time, so an infinitely large
  list can be provided without consuming system memory
- `zip_longest` from `itertools` can be used as an alternative to the `zip`
  consuming up until the shortest list:

  ```python
  xs = [1,2,3]
  string = "hello"
  zs = zip_longest(xs, string)

  for _, z in enumerate(zs):
    print(z)

  # (1,    'h')
  # (2,    'e')
  # (3,    'l')
  # (None, 'l')
  # (None, 'o')
  ```
