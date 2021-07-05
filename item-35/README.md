# Item 35 - Avoid using `throw` for state transitions in generators

```shell
$ python3 ./
```

- a custom `Exception` can be created by subclassing `Exception`:

    ```python
    class MyError(Exception):
        pass

    error = MyError('oh noes!')
    ```
- errors can be thrown from generators:

    ```python
    from itertools import count

    class MyError(Exception):
        pass

    def my_gen():
        for x in count():
            yield x

    it = my_gen()

    try:
        it.throw(MyError('an exception!'))
    except MyError:
        print('errored')

    # errored
    ```
- when a generator throws, subsequent iterations will throw `StopIteration`:

    ```python

    from itertools import count

    class MyError(Exception):
        pass

    def my_gen():
        for x in count():
            yield x

    it = my_gen()

    try:
        it.throw(MyError('an exception!'))
    except MyError:
        print('errored')

    try:
        next(it)
    except StopIteration:
        print('iteration stopped')

    # errored
    ```
- a generator can handle exceptions internally:

    ```python
    from itertools import count

    class MyGenError(Exception):
        pass

    def my_gen():
        for x in count()
            try:
                yield x
            except MyGenError:
                #  do something

    it = my_gen()

    print(next(it))
    # 0

    it.throw(MyGenError('oh noes'))

    print(next(it))
    # 1
    ```
- this allows one to use exceptions to manage state in generators (which should
    not be done!)

    ```python
    class CountdownReset(Exception):
        pass

    def countdown_gen(start: int):
        remaining = start

        while remaining > -1:
            try:
                yield remaining
                remaining = remaining - 1
            except CountdownReset:
                remaining = start

    it = countdown_gen(3)

    print(next(it))
    print(next(it))
    # 3
    # 2

    print('reset')
    it.throw(CountdownReset('reset!')) # code smell

    print(next(it))
    print(next(it))
    # 0
    # 1
    ```
    - this looks like a code smell, and is messy
- instead of using `throw` to hack state into generators, use a class that
    implements `__iter__` instead:

    ```python
    class Countdown():
        def __init__(self, start = 5, /):
            self.start = start
            self.current = self.start

        def reset(self):
            self.current = self.start

        def __iter__(self):
            while self.current > -1:
                try:
                    self.current = self.current - 1
                    yield self.current
                except:
                    self.current = self.start

    countdown = Countdown(3)
    countdown_it = iter(countdown)

    print(countdown.current)
    print(next(countdown_it))
    print(next(countdown_it))
    # 3
    # 2
    # 1

    print('reset')
    countdown.reset()

    print(countdown.current)
    print(next(countdown_it))
    print(next(countdown_it))
    # 3
    # 2
    # 1
    ```
