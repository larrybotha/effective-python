# Item 24 - `None` and Docstrings for dynamic default arguments

```shell
$ python3 ./
```

- the equivalent of `Date.now()` from Javascript in Python is
  `datetime.datetime.now()`:

  ```python
  from datetime import datetime

  time_now = datetime.now()
  ```
- `sleep` is imported from the `time` package
- default values in function declarations are only evaluated once on load. If
  the default value needs to be dynamic, we can't rely on the declaration:

  ```python
  from datetime import datetime
  from time import sleep

  # prints the same time when 'when' is not provided
  def name_time(name: str, when: datetime = datetime.now()):
    print(f"Hey, {name}, it's flippin' {when.strftime('%H:%M:%S')}")

  name_time('Sam')
  sleep(2)
  name_time('Sam')
  # Hey, Sam, it's flippin' 16:36:27
  # Hey, Sam, it's flippin' 16:36:27
  ```
- a Python convention to address this is to use `None` as the default value,
  document the default value in the docstring, and assign the value inside the
  function if it is `None`:

  ```python
  from datetime import datetime
  from time import sleep

  # prints a different time every call
  def name_time(name: str, when: datetime = None):
    if when is None:
      when = datetime.now()

    print(f"Hey, {name}, it's flippin' {when.strftime('%H:%M:%S')}")

  name_time('Sam')
  sleep(2)
  name_time('Sam')
  # Hey, Sam, it's flippin' 16:53:03
  # Hey, Sam, it's flippin' 16:53:05
  ```
- the `Optional` type from `typings` should be used for optional arguments, and
  dynamic arguments that are defaulted to `None`
