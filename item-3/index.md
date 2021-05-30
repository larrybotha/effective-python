# Item 3 - `bytes` and `str`

```
$ python3 main.py
```

- sequences of characters are either of type `bytes`, or `str`
- create a byte string by prepending a string with `b`:
  - `b'my byte string'`
- `list` operates on MutableSequences to split values into a list
- convert `bytes` to `str` using `byte_string.decode()`
- convert `str` to `bytes` using `string.encode('utf-8')`
- concatenate `str` and `bytes` using `+`
  - `b'a' + b'b'`
  - `'a' + 'b'`
- operators common to `str` and `bytes` do not work across types
