# Item 15 - Don't rely on dict insertion order

```
$ python3 ./
```

- Python 3.7 officially supports preserving insertion order of dicts
- writing functions that expect ordered dicts, however, is not a good idea, because
  someone may pass something into your function which is not a dict, yet is
  duck-typed to behave like a dict. e.g. a class that implements
  `MutableMapping` will use a hash type that doesn't preserve insertion order,
  yet could still implement the same interface as `dict`
- in Javascript, objects do not preserve insertion order
- use `sorted` with the `key` parameter to sort values - don't rely on insertion
  order in dicts
- for ordering of dicts, there are three ways to handle this:
  - manually sort using `sorted` and `key`
  - check the type of a value using `instanceof` and throwing if anything other
    than a `dict` is provided
  - add static types and lint the code using something like `mypy` - this will not
    be of any benefit to a module being distributed for others to use, as you are
    responsible for linting your own code
