from inspect import stack
from typing import Optional


def _cr():
    print("")


def _div(text: Optional[str] = "", print_caller: bool = True):
    fn_name = stack()[1][3] if print_caller else None

    print("================")

    if text or fn_name:
        print(text or fn_name)
        _div(print_caller=False)


def _read_path_with_assignment_expression():
    _div()
    my_dict = {}
    path = "some_file.txt"

    if (handle := my_dict.get(path)) is None:
        try:
            handle = open(path, "a+b")
        except OSError:
            print(f"failed to open path: {path}")
            raise
        else:
            my_dict[path] = handle

    handle.seek(0)
    file_data = handle.read()
    print(f"file_data: ({type(file_data)}) {file_data}")
    handle.close()

    _cr()


def _problematic_read_path_with_setdefault():
    _div()
    my_dict = {}
    path = "some_file.txt"

    try:
        # setdefault will always evaluate the fallback,
        # whether the property on is set or not!
        #
        # don't use setdefault for things that use expensive operations
        #
        # furthermore,
        # because this is creating a handle to a file,
        # it'll create
        # multiple handles, which can create conflicts with existing handles
        #
        # it will be difficult to differentiate between exceptions thrown for
        # `open` vs those raised by `setdefault`
        handle = my_dict.setdefault(path, open(path, "a+b"))
    except OSError:
        print(f"failed to open path: {path}")
        raise
    else:
        handle.seek(0)
        file_data = handle.read()
        print(f"file_data: ({type(file_data)}) {file_data}")
        handle.close()

    _cr()


def _using___missing___for_default_values():
    _div()

    def open_file(path: str):
        try:
            return open(path, "a+b")
        except OSError:
            print(f"failed to open path {path}")
            raise

    class MyDictWithDefaults(dict):
        # if a key doesn't exist, set it
        def __missing__(self, key):
            value = open_file(key)
            self[key] = value

            return value

    my_dict = MyDictWithDefaults()
    handle = my_dict["foo"]
    handle.seek(0)
    file_data = handle.read()
    print(f"file_data: ({type(file_data)}) {file_data}")
    handle.close()
    _cr()


if __name__ == "__main__":
    _read_path_with_assignment_expression()
    _problematic_read_path_with_setdefault()
    _using___missing___for_default_values()
