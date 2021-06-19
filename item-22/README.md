# Item 22 - Variable-positioned arguments

```
$ python3 ./
```

- Variable-positioned arguments are called _varargs_ or _star args_: `*args`
- varargs make functions variadic:

  ```python
  # arity of 2 - xs is required
  def my_func_1(message: str, xs: list):
      print(f'{message}: {xs}')

  # variadic - only message is required
  def my_func_2(message: str, *args):
      print(f'{message}: {args}')
  ```
- `*args` is a tuple
- iterables may be spread into functions that accept varargs:

  ```python
  def my_func(msg: str, *args):
      print(msg, args)

  xs = [1,2,3]

  my_func('foo', *xs)
  ```
- because `*args` is a tuple, every value in the iterable will be consumed,
  which can be expensive. Some iterables are lazy and infinite - your
  application would run out of memory

  ```python
  def get_gen():
      for i in range(10);
          yield i

  def my_fn(*args):
      print(args)

  iterator = get_gen()
  # entire generator will be consumed
  my_fn(*iterator)
  ```

  - reserver `*args` for situations where you know the length of the iterable
    will be small
- if a function that accepts variable-positioned arguments is modified to accept
  an additional positioned argument, it can break call-sites, but without
  raising errors
  - avoid using `*args` without keyword-only arguments
