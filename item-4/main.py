from math import pi
from typing import (Optional)

def cr():
  print('')

def div(text: Optional[str] = ''):
  print('================')
  if text:
    print(text)
    div()

def formatted():
  div('formatted')

  key = 'my_var'
  value = pi

  # !r will print the string using the __repr magic method of the variable
  # < sets the right pad, > would set the left pad
  # .2f sets the number of decimal places to 2
  print(f'{key!r:<10} = {value: .2f}')

def multi_line():
  div('multiline')
  # create a list of tuples
  pantry = [ ('eggs', 2), ('rice' ,1) ]

  for i, (item, count) in enumerate(pantry):
    # accepts arguments without commas...?
    print(
        f'#{i+1}: '
        f'{item.title():<10s} = '
        f'{round(count)}'
    )

if __name__ == '__main__':
  formatted()
  cr()
  multi_line()
