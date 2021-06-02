# Item 6 - Prefer multiple assignment unpacking over indexing

```
$ python3 main.py
```

- python has a built-in tuples
- key value pairs can be obtained from dicts in a similar manner to Javascript's
  `Object.items(someObj)` does:

  ```python
  some_dict = {'a': 1', 'b': 2}
  print(some_dict.items())
  # dict_items([('a', 1), ('b', 2)])
  ```
- items in a tuple are accessed using indexes in the same way that items in
  arrays are accessed
- items in a tuple may not be reassigned:

  ```python
  my_tuple = (1,2,3)
  my_tuple[0] = 4
  # throws TypeError
  ```
- items can be unpacked from tuples:

  ```python
  t = (1,2,3)
  first, second, third = t

  d = {'foo': ('bar', 1)}
  ((name, (key, val))) = d.items()
  ```
- unpacking can be used to swap values:

  ```python
  xs = [1,2]
  xs[1], xs[0] = xs

  # or generally
  xs = list(range(10))
  for i in xs:

  ```
- unpacking can be useful in loops:

  ```python
  d = {
    'foo': ('bar', 1),
  }

  for  (name, (x, y)) in d:
    print(f'{name}: ({x}, {y}))')

  l = [('foo', 1), ('bar', 2)]

  for x, y in l:
    print(f'{x} => {y}')
  ```
- `enumerate`'s 2nd value accepts a starting index, which only affects the value
  of the index in a loop, and not the index of the array being operated on:

  ```python
  l = ['a','b','c']

  # start index at 1
  for index, char in enumerate(l, 1):
    print(f'{index}: {char}')

  # 1: a
  # 2: b
  # 3: c
  ```
