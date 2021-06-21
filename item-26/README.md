# Item 26 - Function decorators with `functools.wraps`

```shell
$ python3 ./
```

- decorators are functions that run before and after the function they decorate
- they can modify inputs, outputs, and raise exceptions
- to define a decorator:

  ```pythonn
  def my_decorator(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      # ... do something with result

      return result

    return wrapper
  ```
- `def wrapper(*args, **kwargs):` can be interpreted as "get all positional
  arguments, get all keyword arguments". This will likely be how one would
  define a custom `curry` function
- if the closure inside the decorator isn't itself decorated with
  `functools.wraps`, the metadata  of the decorated function passed into the
  decorator will be lost. i.e. `decorated_func['__name__' | '__doc__']` or
  `help(decorated_func)` etc. will yield the closure's metadata
- use `functools.wrap` to create decorators that retain the decorated function's
  metadata:

  ```python
  from functools import wraps

  def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      # decorate function
  ```
  - `wraps` copies all of the metadata from the decorated function to the
    wrapped function
