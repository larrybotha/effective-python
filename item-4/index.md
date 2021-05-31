# Item 4 - Interpolated strings

```
$ python3 main.py
```

- left and right padding can be set in formatted strings using `:<` and `:>`
  - pad right to occupy 10 characters of space:

    ```python
    my_var = 'foo'
    padded_right = f'{my_var:<10} hello'
    # foo       hello
    ```
  - pad left to occupy 10 characters of space:

    ```python
    my_var = 'foo'
    padded_right = f'{my_var:>10} hello'
    #        foo hello
    ```
- numbers can be formatted to a determined number of decimal places using `.[digit]f`

  ```python
  two_decimals = f'{math.pi: .2f}'
  ```
