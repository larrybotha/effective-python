# Item 7 - Prefer `enumerate` over `range`

```
$ python3 main.py
```

- its common to iterate over iterables using `range` and `len`, but it's clumsy:

  ```python
  xs = [1,2,3]

  for i in range(len(xs)):
    print(f'{i}: {xs[i]}')
  ```
- `enumerate` wraps iterators with a lazy generator, and makes for much more
  succinct code:

  ```python
  xs = [1,2,3]

  for i, x in enumerate(xs):
    print(f'{i}: {x}')
  ```
- as in Javascript, a generator can be iterated on manually using `next`:

  ```python
  xs = [1,2,3]
  iterator = enumerate(xs)

  print(next(iterator))
  # (0, 1)
  # [1][2]
  #
  # 1 - index
  # 2 - value at index
  ```
- `enumerate` also allows the starting value of the index to be supplied:

  ```python
  xs = ['a','b','c']
  start_index = 1

  for i, char in enumerate(xs, start_index):
    print(f'{i} => {char}')

  # 1 => a
  # 2 => b
  # 3 => c
  ```
