# Item 16 - Prefer `get` over `in` for missing key values

```
$ python3 ./
```

- accessing missing keys in `dict`s will throw in Python, unlike in Javascript
- `dict.get` will safely return `None` if the key isn't present
- `dict` throws a `KeyError` exception when attempting to access a key that
  isn't present
- Python has a `Counter` class in the `collections` module, if managing counters
- `get` can be used to retrieve a value with a fallback, but `setdefault` can be
  used to assign a value if a key isn't present:

  ```python
  my_dict = get_dict()
  # set foo to bar if foo  is not present
  my_dict.setdefault('foo', 'bar')
  ```
- values assigned via `dict.setdefault` are assigned by reference! Make sure to
  copy values in for purity

  ```python
  my_dict = {}
  key = "foo"
  xs = []

  my_dict.setdefault(key, xs)
  xs.append(1)

  # my_dict["foo"] => [1]
  ```
- `setdefault` is not actually great to use - `defaultdict` is a superior
  alternative for working with dicts that need default values
