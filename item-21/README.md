# Item 21 - Closures and variable scope

```
$ python3 ./
```

- functions are first-class in Python
- the function passed to `key` in `sorted` that allows for customising the
  sorting of values requires that a tuple be returned. The first value is the
  index at which to compare the value at, and the second is the value itself

  ```python
  # create 2 groups of values (only 2 tuples) to sort values by
  def sort_by_bound(bound: int):
    def helper(x: int):
      return (0, x) if x > bound else (1, x)

    return helper

  xs = [random.randint(0,10) for _ in range(10)]

  # group values either side of 5
  print(sorted(xs, key=sort_by_bound(5)))
  # => [6, 6, 7, 7, 8, 9, 10, 3, 4, 5]
  ```
- `NameError` is raised when attempting to access a variable that is not in
  scope. This is equivalent to Javascript's `ReferenceError`
- Python doesn't reassign values found in closures:

  ```python
  def my_func():
      x = 'foo'

      def inner():
          x = 'bar'

      inner()

      print(x)
      # => foo
  ```
- to allow functions to modify variables in their outer scope, one needs to
  indicate to Python that it's a non-local variable using `nonlocal`

  ```python
  def my_func():
    x = 'foo'

    def inner():
      nonlocal x
      x = 'bar'

      inner()

    print(x)
    # => foo
  ```
- avoid using `nonlocal` - it's impure, and can also make for difficult
  debugging
- also, avoid shadowing variable names, even though Python protects one from it
- Python allows for instances of classes to be callable by defining a `__call__`
  method:

  ```python
  class Callable:
      def __init__(self, name: str):
          self.name = name

      def __call__(self):
          print(f"call me {self.name}")

  callable = Callable('Al')
  callable()
  ```
