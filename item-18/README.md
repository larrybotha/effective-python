# Item 18 - Construct key-dependent values with `__missing__`

```
$ python3 ./
```

- there are a number of ways to deal with default values in dicts:
  - use `dict.setdefault`
  - use `collections.defaultdict` if you control the dict
  - use `__missing__`
- `dict.setdefault` will always call the statement in the fallback:

  ```python
  my_dict = {}
  my_dict.setdefault('a', 'foo')

  # prints 'bar' even though 'a' is set
  my_dict.setdefault('a', print('bar'))
  # => bar
  ```
  - don't use `setdefault` with expensive operations!
- Python allows for subclassing `dict` with a `__missing__` method, which can be
  used to set a default value on a dict if a property that doesn't exist on the
  dict is accessed:

  ```python
  class DictWithMissing(dict):
    def __missing__(self, key):
      value = 'quux'
      self[key] = value

      return value

  my_dict = DictWithMissing()
  my_dict['foo']
  # => 'quux'
  ```
