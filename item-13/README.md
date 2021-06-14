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
- unpacking with a catch-all is only allowed when there is at least one other
  assigned value unpacked, too:

  ```python
  xs  = [1,2,3]
  *unpacked = xs # not allowed
  ```
- catch-all unpacking can be used with arbitrary iterators:

  ```python
  def generate_csv_data():
    yield ("header 1", "header 2", "header 3")
    yield ('row 1 value 1', 'row 1 value 2', 'row 1 value 3')
    yield ('row 2 value 1', 'row 2 value 2', 'row 2 value 3')
    # ...

  header, *rows = generate_csv_data()
  ```
- unpacking will load the entire iterable into memory - so it it's arbitrarily
  large, it's likely a good idea not unpack it, and rather to use generator
  features to iteratively recurse over the data
