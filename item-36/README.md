# Item 36 - `itertools` and working with iterators and generators

```shell
$ python3 ./
```

- use `help(itertools)` to see if `itertools` has any useful tools for working
    with complex or tricky iterators
    - `cycle` - emit values from an iterable indefinitely - similar to `replay`
        in `RxJs`

        ```javascript
        import {from} from 'rxjs'
        import {repeat} from `rxjs/operators`

        const stream = from([1,2,3])
        const repeatStream = stream.pipe(repeat())

        // -1--2--3--1--2--3-->
        ```

    - `repeat` - emits the same value indefinitely, similar to `constant` in
        `RxJs`
    - `count` - emits sequential numbers from a starting point
    - `zip_longest` - `zip`, but will only emit `StopIteration` when the longest
        iterable completes
    - `islice` - iterator slice - slice arbitrary iterable values using a
        similar syntax to `xs[start:end:step]`, but doesn't support `Reverse`
    - `chain` - append an iterator onto another, similar to `concat` in
        Javascript arrays, or in `RxJs`:

        ```javascript
        import {concat, from} from 'rxjs'

        const x1 = from([1,2,3])
        const x2 = from([4,5,6])
        const xs = concat(x1, x2))

        # -1--2--3--4--5--6--|
        ```
    - `chain.from_iterable`, which behaves like `flatten` in Javascript:

        ```python
        from itertools import chain

        xxs = [[1,2,3], [4,5,6]]
        iter = chain.from_iterable(xxs)

        for x in iter:
            print(x)

        # 1, 2, 3, 4, ...
        ```
    - `tee` - create `n` multiple independent iterators from a single iterator
    - `dropwhile` - drops values from an iterator until a condition is met
    - `takewhile` - takes values from an iterator until a condition is met
    - `filterfalse` - inverse of the built-in `filter`
    - `accumulate` - similar to `RxJs`s `scan`, emitting a value on each
        iteration of the accumulating function
    - `starmap` - apply a function to an iterable
    - `compress` - apply a boolean-like iterator to each value of a source iterator
        to filter it
    - `product` - generate a cartesian product from iterables
    - `permutations` - generates permutations of iterables
    - `combinations` - generates combinations of iterables
- `itertools` splits its tools into 3 main categories:
    - infinite iterators
    - iterators that operate on iterables
    - iterators that produce combinations of iterables
