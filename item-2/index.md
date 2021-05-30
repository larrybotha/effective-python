# Item 2 - PEP8

```
$ python main.py
```

- don't check for empty values using `len(someValue)` - empty values will evaluate to
  false implicitly
  - this is in contrast to Javascript, where `[]` and `{}` are truthy
- don't check for non-empty values in the same way - non-empty values will
  evaluate to true implicitly
