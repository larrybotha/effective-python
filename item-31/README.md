# Item 31 - Iterate over arguments defensively

```shell
$ python3 ./
```

- attempting to iterate over an iterator that has already raised `StopIteration`
  with `list`, `for`, or some other operation for iterating will not yield an
  error, because `StopIteration` is expected. An empty list will always be
  returned

  ```python
  def my_gen():
    yield True

  g = my_gen()

  list(g)
  # => [True]
  list(g)
  # => []
  list(g)
  # => []
  ```
- if an iterator is passed to a function that consumes that iterator at any
  point, any further attempts to read from the iterator will yield no values

  ```python
  def do_something(xs: Iterable):
      # sum will consume the iterator
      total = sum(xs)

      # there'll be nothing to read from the iterator at this point
      for x in xs:
          # ...

      # ...
  ```
- some ways to address this:
  - create a copy of the iterator
    - this undermines the value of using a generator - large lists are going to
      occupy a lot of memory
  - pass in a generator using a lamda:

    ```python
    def do_something(gen_fn: Callable):
        total = sum(gen_fn())

        for x in gen_fn():
            # ...

    def my_gen(length: int = 3):
        for x in range(length):
            yield x

    do_something(lambda: my_gen(5))
    ```
    - this is kinda clumsy
  - use a class that implements `__iter__`
  - reject arguments that are iterators
- `list`, `for` loops, and things that iterate over iterables are making use of
  `__iter__` on the iterables to loop over values
- `__iter__` must return an iterator function, which must implement the
  `__next__` method
- creating a class that implements `__iter__` makes that class iterable:
  ```python
  class MyIterable:
    def __init__(self, length: int):
      self.length = length

      def __iter__(self):
        return range(self.length)

  it = MyIterable(3)

  list(it)
  # [0, 1, 2]

  list(it)
  # [0, 1, 2]
  ```
- a class that implements `__iter__` using a generator can handle arbitrarily
  large sequences without iterators consuming and preventing access to the
  sequence in subsequent iterations:

  ```python
  class MyFileIterable:
      def __init__(self, path: string):
          self.path = path

      # every time this object is iterated over, return a new iterator
      def __iter__(self):
          with open(self.path, 'r') as file_handle:
              for line in read(file_handle):
                  yield line

  it = MyFileIterable("foo.txt")

  list(it)
  # ["line 1", "line 2", "line 3"]

  list(it)
  # ["line 1", "line 2", "line 3"]
  ```
  - this has the downside that the file is being read twice
- lastly, we can reject an argument if it is an iterator:

  ```python
  def defensively_do_something(xs):
      # iter will return the iterator if passed in
      if iter(xs) === xs:
        raise TypeError('Only containers allowed')

      total = sum(xs)

      for x in xs:
          # ...
  ```
  - this allows us to pass in an instance of the `MyIterable` class above, which
    will ensure the iterator is never consumed further down in the function body
- if an iterator is passed to `iter`, it will return that iterator, otherwise
  it'll return a new iterator - this can be used to check if a value is an
  iterator or not
- alternatively, one can use `isinstance` with `collection.abc.Iterator`:

  ```python
  from collections.abc import Iterator

  def is_iterator(xs):
    return isinstance(xs, Iterator)
  ```
