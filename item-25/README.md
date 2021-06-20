# Item 25 - Clarity, keyword-only, and position-only arguments

```shell
$ python3 ./
```

- functions in Python are by default interchangeably usable as positional or
  keyword arguments
  - mixing keyword and positional arguments requires that the keyword arguments
    come before positional arguments
- functions that allow keyword arguments may not be able to easily change the
  names of those arguments in future
- functions that allow positional arguments may not be able to easily change the
  order of those arguments in future
- an `OverflowError` is raised when there is an attempt to generate a value
  larger than what the associated type can store

  - `math.exp(1000)` - `e` raised to 1000 creates a float that is too large
- functions with subtly different arguments, such as multiple booleans, can be
  difficult to remember at which position to put a value
  - if a function is going to throw for special values, parameters can be set to
     defaults that throw for those special characters, and users can explicitly
     override those arguments if they need to
- if a function has special flags or values, it may be beneficial to enforce
  that those values may only be passed via keywords
  - separating arguments with a `*,` indicates that any arguments following the
    `*` may only be passed using keywords

    ```pythonn
    # allow_zero_division may only be specified as a keyword argument
    def my_div(num: float, den: float, *, allow_zero_division = False):
      # ...
    ```

  - passing these values as positional arguments will raise a `TypeError`
- arguments can be made positional only by delimiting the list of positional
  arguments with a `/`:

  ```python
  # a and b may only be passed as positional arguments
  def my_sum(a:int, b: int, /):
    return a + b
  ```

  - this allows one to change the name of parameters to functions without
    breaking call-sites
- position-only and keyword-only symbols can be used together:

  ```python
  # key_or_pos1 and key_or_pos2 behave like arguments do in Python by default -
  # they may be specified positionally or by keyword
  def my_func(pos_1, pos2, /, key_or_pos1, key_or_pos2, *, key_1, key_2):
    # ...
  ```
