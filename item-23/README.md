# Item 23 - Optional behaviour with keyword-arguments

```shell
$ python3 ./
```

- avoid using positional arguments for optional arguments - always use keyword
  arguments as it makes the intent at the call-site clear
- keyword arguments make it clear what a function is being called with
- keyword arguments can have default values defined in the function definition,
  making those parameters optional
- keyword arguments make extending functions easy while retaining backwards
  compatibility
- arguments can be passed to functions in 3 ways:
  - positioned: `my_func(a, b)`
  - variable positioned: `my_func(*args)` (if the function supports
    variable-positioned arguments)
  - keyword: `my_func(a = 1, b = 2)`
- keyword-arguments can be used with any function that defines positioned
  arguments:

  ```python
  def add(first: float, second: float):
      return first + second

  add(first = 1, second = 2)
  # is equivalent to
  add(1,2)
  ```
- order of keyword arguments doesn't matter

  ```python
  def add(first: float, second: float):
    return first + second

  add(first = 1, second = 2)
  # is equivalent to
  add(second = 2, first = 1)
  ```
- dicts can be used for keywork arguments using the `**kwargs` syntax:

  ```python
  def add(first: float, second: float):
    return first + second

  my_dict = {
    'first' = 1,
    'second' = 2
  }

  add(**my_dict)
  ```
- `**kwargs` can be mixed with keyword args:

  ```python
  def add(first: float, second: float):
    return first + second

  my_dict = {
    'first' = 1,
  }

  add(**my_dict, second = 2)
  ```
- `**kwargs` can be mixed with other `**kwargs`:

  ```python
  def add(first: float, second: float):
    return first + second

  my_dict_1 = { 'first' = 1 }
  my_dict_2 = { 'second' = 2 }

  add(**my_dict_1, **my_dict_2)
  ```
- `**kwargs` arguments:
  - cannot share keyword arguments in the same function call
  - cannot share properties with other kwargs in the same function call
