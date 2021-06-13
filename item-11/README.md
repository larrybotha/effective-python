# Item 11 - Slicing sequences

```
$ python3 ./
```

- slices have the form `[start:stop:step]`
- copy a list: `[:]`
- slice from index n in a list: `[n:]`
- slice to index n in a list: `[:n]`
- skip items in a list using `step` `[::2]`
- reverse a list using `[::-1]`
- sets and tuples can be sliced using `itertools.islice`
- lists can be modified in-place with slices:

  ```python
  xs = [1,2,3,4]
  xs[2:] = ['c','d']

  # => [1,2,'c','d']
  ```
