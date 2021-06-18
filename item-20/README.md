# Item 20 - Prefer raising exceptions over returning `None`

```
$ python3 ./
```

- [Dead Simple Python - errors][dsp-errors] makes a great case for becoming
  comfortable with exceptions in Python
- if under normal circumstances a function returns one type, and then under some
  special circumstance returns `None`, this is likely a code smell. Raise an
  exception if a contract is violated, don't return a falsy value that can be
  interpreted incorrectly:

  ```python
  def divide(x: float, y: float) -> float:
    try:
      return x / y
    except ZeroDivisionError:
      # NO! None is falsy, so is 0. 0 is a valid result for this function, None
      # is not
      return None
  ```
- type signatures will shout at you if you attempt to mix return types. Use
  them! Try avoiding mixing of return types if a valid return type can be
  evaluated to a falsy value
- `ZeroDivisionError` is raised when dividing by 0
- raise exceptions for special cases - don't return a different type:

  ```python
  try:
    # do something
  except SomeError as error:
    raise MyError('This thing happened') from error
  ```
- explicit exception chaining allows for our own raised exceptions to be
  associated with the actual raised error, using the `from` syntax:

  ```python
  try:
    # ...
  except ZeroDivisionError as error:
    raise ValueError('0 denominator provided') from error
  ```

  - evaluating `error.__cause__` reveals how with the chained exception we can
    see the original error
- docstrings should contain `Raises` sections describing what a function could
  potentially raise:

  ```python
  def my_div(x: float, y: float) -> float:
      """my_div
      ...
      Raises:
          ValueError: when providing 0 denominator

      ...
      """
  ```
- expect calling functions to properly handle exceptions

<!-- LINKS -->
[dsp-errors]:
  https://dev.to/codemouse92/dead-simple-python-errors-l82 "Dead Simple Python - Errors"
