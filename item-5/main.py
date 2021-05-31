from typing import (Optional)
from urllib.parse import parse_qs

def cr():
  print('')

def div(text: Optional[str] = ''):
  print('================')
  if text:
    print(text)
    div()

def get_first_int(values: dict, key: str, default: int = 0):
  xs = values.get(key, [''])

  # if-else is easier to read than using "or / and" statements
  if xs[0]:
    return int(xs[0])

  return default

def example_1():
  div("parse_qs")
  qs="red=4&blue=0&green="
  values = parse_qs(qs, keep_blank_values = True)
  print(f'for query string {qs}')
  cr()

  print("with values.get:")
  # gets different types of values - list[str] | None
  print(f'{"Red":<10} {values.get("red")}')
  print(f'{"Blue":<10} {values.get("blue")}')
  print(f'{"Green":<10} {values.get("green")}')
  print(f'{"Opacity":<10} {values.get("opacity")}')
  cr()

  print("with get_first_int:")
  print(f'{"Red":<10} {get_first_int(values, "red")}')
  print(f'{"Blue":<10} {get_first_int(values, "blue")}')
  print(f'{"Green":<10} {get_first_int(values, "green")}')
  print(f'{"Opacity":<10} {get_first_int(values, "opacity")}')
  cr()

if __name__ == '__main__':
  example_1()
