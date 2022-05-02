# Item 46 - Descriptors for reusable `@property` methods

```shell
$ python3 ./
```

- `@property` is good for defining getters and setters for a single property
  with validation
- `@property` is not so good for multiple properties that should behave in the
  same manner - i.e. reusing logic in `@property` is not possible - the same
  logic must be defined repeatedly
- using a descriptor class to define shared behaviour of properties within a
  class can be superior
- **NB**: descriptors are assigned as class attributes!
- to define a descriptor class, create a class that defines a `__set__` and
  `__get__` method:

  ```python
  def MyDescriptor:
      def __get__(self, instance, instance_type):
          pass

      def __set__(self, instance):
          pass
  ```

- given the following code:

  ```python
  class MyDescriptor:
      def __init__(self, value = 0, /)
          self._value = value

      def __get__(self, instance, instance_type):
          return self._value

      def __set__(self, instance, value):
          self._value = value

  class MyClass:
      some_value = MyDescriptor()

  # 1 - create instance
  class_instance = MyClass()

  # 2 - assign attribute
  class_instance.some_value = 5

  # 3 - get attribute
  print(class_instance.some_value)
  # => 5
  ```

  - assigning the attribute (#2) is interpreted as follows:

    ```python
    MyClass.__dict__['some_value'].__set__(class_instance, 5)
    ```

  - getting an attribute (#3) is interpreted as follows:

    ```python
    MyClass.__dict__['some_value'].__get__(class_instance, MyClass)
    ```

  - Python does the following when accessing or assigning attributes:

    1. checks if an instance has the attribute
    2. checks the instance's class for the attribute
       - if the attribute implements the descriptor interface, i.e. it
         defines a `__get__` and `__set__` method, Python assumes you
         want to follow the descriptor protocol

    i.e.

    ```python
    class_instance.some_value

    # first evaluate class instance:
    # class_instance.__dict__['some_value']

    # else evaluate class itself:
    # MyClass.__dict__['some_value']
    # or
    # class_instance.__class__.__dict__['some_value']
    ```

  - property access is similar here to Javascript's prototypal inheritance /
    delegation

- beware when using descriptors with an `__init__` - the init is called when the
  class is evaluated, and behaves as a class attribute:

  ```python
  class MyDescriptor:
      def __init__(self, value = "foo", /):
          self._value = value

      def __get__(self, *_):
          return self._value

      def __set__(self, instance, value, /):
          self._value = value

  class MyClass:
      value = MyDescriptor()

  instance_1 = MyClass()
  instance_2 = MyClass()

  instance_1.value = "bar"

  # instance_2 will have the following:
  # instance_2.value == "bar"
  ```

  Descriptors are useful for computing values from existing instance
  properties, so relying on `__init__`, unless setting a value for a class
  attribute, is not going to work as expected

- to ensure that attributes are attribute-specific with descriptors, one
  should use `WeakKeyDictionary` to store values for all the instances
  inside the descriptor (an example demonstrating a memory leak, as a
  result of using a `dict` to store references to instances, can be seen
  in the examples)

  ```python
  from weakref import WeakKeyDictionary

  class MyDescriptor:
      def __init__(self):
          # this prevents references to instances being retained when instance
          # counts reach zero, as opposed to using dict
          self._values = WeakKeyDictionary()

      def __get__(self, instance, _):
          if instance is None:
              return self

          return self._values.get(instance, "default value")

      def __set__(self, instance, value):
          self._values[instance] = value
  ```

  - `WeakKeyDictionary` holds weak references to objects - when there are no
    more strong references to objects, i.e. the object is no longer used
    elsewhere, the value in the `WeakKeyDictionary` will be garbage
    collected, as opposed to if we used a `dict` or something that would
    hold a strong reference to the value
