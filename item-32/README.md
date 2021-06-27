# Item 32 - Generator expressions for large comprehensions

```shell
$ python3 ./
```

- one can open files using list comprehensions:

    ```python
    lines = [line for line in open('some-file.txt')]
    ```
- a generator expression can be used to do the same thing:

    ```python
    line_iterator = (line for line in open('some-file.txt'))
    lines = []

    while True:
        try:
            lines.append(next(line_iterator))
        except StopIteration:
            break;
    ```
- this allows one to benefit from the brevity of comprehensions with the memory
    efficiency of generators
- generator comprehensions can be composed:

    ```python
    from itertools import count

    ord_a = ord('a')
    count_iterator = count(0)
    chr_iterator = (chr(ord_a + x) for x in count_iterator)

    # advance chr_iterator
    next(chr_iterator)
    # => a

    # advance counter_iterator
    next(count_iterator)
    # => 1

    # advance chr_iterator
    next(chr_iterator)
    # => c (i.e. not b)

    ```
    - advancing one iterator will advance the other
- generator expressions are a good choice when memory is important
