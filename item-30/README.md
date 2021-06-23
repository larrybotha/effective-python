# Item 30 - Consider using generators instead of returning lists

```shell
$ python3 ./
```

- generators hold state implicitly
- one must take care when reusing an iterator returned from a generator - they
  do not behave like lists
- a list can be created from an iterator by passing the iterator to `list`
- generators are functions which contain the `yield` keyword
- generators don't consume entire lists, and so can be used on streaming data,
  or very large lists, without consuming massive amounts of memory

## Resources

- [When to use generators in Python][when-to-use-generators]


[when-to-use-generators]:
  http://thepythoncorner.com/dev/generators-in-python-should-i-use-them/
  "When to use generators in Python"
