# Item 30 - Consider using generators instead of returning lists

```shell
$ python3 ./
```

- generators hold state between calls
- when a generator completes, it raises `StopIteration`
- one must take care when reusing an iterator returned from a generator - they
  do not behave like lists
- a list can be created from an iterator by passing the iterator to `list`
- generators are functions which contain the `yield` keyword
- generators don't consume entire lists, and so can be used on streaming data,
  or very large lists, without consuming massive amounts of memory
- from [this article][when-to-use-generators], ask not "When to use a
  generator", but instead "when not to use a generator"
- Iteratables, iterators, and generators:
  - an iterable is an object that implements `__iter__`, and can be looped over.
    e.g. lists, sets, dicts, tuples, etc.
  - an iterator is a subclass of an iterable, and pauses processing of subsequent
  values in a sequence until the current value has been processed. Iterators
  have the `__next__` method in addition to `__iter__`
  - a generator is a function that makes use of a `yield` statement to lazily
    return values in arbitrary sequences without consuming the entire sequence
    on initialisation. Generators produce iterators

- use `os.path` to get path information
  - basename of file: `os.path.basename`
  - dirname of file: `os.path.dirname`

## Resources

- [When to use generators in Python][when-to-use-generators]
- [Iterable vs Iterator vs Generator in Python][iteratable-iterator-generator]
- [Iterators and generators][iterators-and-generators]


[when-to-use-generators]:
  http://thepythoncorner.com/dev/generators-in-python-should-i-use-them/
  "When to use generators in Python"
[iteratable-iterator-generator]:
  https://python.plainenglish.io/iterable-vs-iterator-vs-generator-in-python-6798cdae511c+
  "Iterable vs Iterator vs Generator in Python"
[iterators-and-generators]:
  https://www.analyticsvidhya.com/blog/2020/05/python-iterators-and-generators/
  "Iterators and generators"
