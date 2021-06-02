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
  qs="apples=4&pears=0&oranges="
  values = parse_qs(qs, keep_blank_values = True)
  print(f'for query string {qs}')
  cr()

  print("with values.get:")
  # gets different types of values - list[str] | None
  print(f'{"Apples":<10} {values.get("apples")}')
  print(f'{"Pears":<10} {values.get("pears")}')
  print(f'{"Oranges":<10} {values.get("oranges")}')
  print(f'{"Nada":<10} {values.get("nada")}')
  cr()

  print("with get_first_int:")
  print(f'{"Apples":<10} {get_first_int(values, "apples")}')
  print(f'{"Pears":<10} {get_first_int(values, "pears")}')
  print(f'{"Oranges":<10} {get_first_int(values, "oranges")}')
  print(f'{"Nada":<10} {get_first_int(values, "nada")}')
  cr()

if __name__ == '__main__':
  example_1()
