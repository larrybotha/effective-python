# Item 19 - Unpack a maximum of 3 values when functions return multiple values

```
$ python3 ./
```

- assertions can be made using `assert`:

  ```python
  my_val = 1

  assert my_val == 2
  ```

  - `assert` raises an `AssertionError`
- when unpacking from a long list of return values, unpack no more than 3
  values, using the dynamic positioning of the unpacking operator
- when writing functions that return multiple values:
  - never return more than 3 values
  - if there are more than 3 values to return:
    - return a named tuple, or
    - return a small class containing the values
