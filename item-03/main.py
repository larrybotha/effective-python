from typing import (Union, Optional)

def div(text: Optional[str] = ''):
  print('================')
  if text:
    print(text)
    div()

def to_str(text: Union[bytes, str]):
  result = text

  if isinstance(text, bytes):
    print(f"{text} is isinstance of bytes")
    result = text.decode()

  return result

def to_bytes(text: Union[bytes, str]):
  result = text

  if isinstance(text, str):
    print(f"{text} is isinstance of str")
    result = text.encode('UTF-8')

  return result

if __name__ == '__main__':
  string = 'hello'
  byte_string = b'h\x65llo'

  div("bytes vs str")

  for x in [string, byte_string]:
    print(f"value: {x}")
    print(f"as list: {list(x)}")
    print(f"type: {type(x)}")
    print("\n")

  div("to_str")

  for x in [string, byte_string]:
    print(f"before: {x} is {type(x)}")
    result = to_str(x)
    print(f"after: {result} is {type(result)}")
    print("\n")

  div("to_bytes")

  for x in [string, byte_string]:
    print(f"before: {x} is {type(x)}")
    result = to_bytes(x)
    print(f"after: {result} is {type(result)}")
    print("\n")

  div("bytes and str comparisons evaluate to false")
  print(f"'foo' == b'foo': {'foo' == b'foo'}")
