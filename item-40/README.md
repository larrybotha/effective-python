# Item 40 - `super` for initialising parent classes

```shell
$ python3 ./
```

- multiple inheritance should be avoided (favour composition over inheritance)
- classes making use of multiple inheritance have multiple values in the class
    definition:

    ```python
    class One:
        pass

    class Two:
        pass

    class Multiple(One, Two):
        pass
    ```
-
