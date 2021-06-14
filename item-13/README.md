# Item 13 - Favour catch-all unpacking over slicing

```
$ python3 ./
```

- Like JS, Python has a similar _rest_ syntax for unpacking, called catch-all
  unpacking:

  ```python
  xs = list(range(1000))
  first, *rest = xs
  ```
- unlike, JS, it's not limited to the end of an iterable:

  ```python
  xs = list(range(1000))
  first, *middle, last = xs
  ```
- whenever an index or slice is used to get an iterables values, consider using
  catch-all unpacking
