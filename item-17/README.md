# Item 17 - Prefer `defaultdict` over `setdefault`

```
$ python3 ./
```

- if you don't control a dict, using `setdefault` can be a terse way to add
  values to dicts:

  ```python
  place_map = {"countryA": {"city1", "city2"}, "countryB": {"city2", "city3"}}

  # verbose with dict.get
  if (new_place := place_map.get("countryC")) is None:
      place_map["countryC"] = new_place = set()
      new_place.add("city5")

  # terse with setdefault
  country_d = place_map.setdefault("countryD", set())
  country_d.add("city6")
  ```
- if you _do_ control the dict, such as managing state inside your own class,
  `defaultdict` can be a better choice:

  ```python
  my_dict = defaultdict(factory_for_value)
  ```
