# Item 34 - Avoid using generators' `send` method to inject data

```shell
$ python3 ./
```

- `yield` statements evaluate to `None`

  ```python
  def gen(length: int):
      for i in range(length):
          result = yield i
          print(f'result: {result}')

  it = gen(2)

  while True:
      try:
          output = next(it)
          print(f"yielded: {output}")
      except StopIteration:
          break

  # yielded: 0
  # result: None
  # yielded: 1
  # result: None
  ```
