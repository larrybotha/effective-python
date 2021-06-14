# Item 14 - Sort complex criteria using the `key` parameter

```
$ python3 ./
```

- iterables can be sorted using the `key` parameter in `sorted` and `.sort`
  expressions:

  ```python
  xs = [{'name': 'z', 'value': 2}, {'name': 'a', 'value': 3}]
  sorted_xs = sorted(xs, key=lambda x: x['name'])
  ```
- lambdas have the following structure:

  ```python
  lambda value: expression
  ```
- the lambda can be used to apply additional processing on the values before
  sorting, .e.g converting to lower-case, etc.

  ```python
  places = ["Paris", "Amsterdam", "Rotterdam"]
  print(f"{'sorted:':>10} {sorted(places, key=lambda x: x.lower())}")
  ```
- multiple keys can be provided to determine more complex sort orders:

  ```python
  sorted(items, key=lambda x: (x.key1, x.key2))
  ```
- sorting can only happen in one direction, so attempting to sort in reverse for
  one property, and forwards for another is not possilbe. Python supports
  _stable_ sorting, meaning the same item can be sorted in multiple statements,
  and previous sorts will be maintained
