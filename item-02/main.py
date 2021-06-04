if __name__ == '__main__':
  print(str.strip(f"""
      don't check for emptiness of values using len(x) == 0 or other methods
      """))
  print("empty values evaluate to False")

  # bad
  if len([]) == 0: pass
  # good
  if []: pass

  # bad
  if len("") == 0: pass
  # good
  if "": pass

