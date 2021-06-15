from collections import defaultdict
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


def _terse_setdefault_vs_long_get():
    _div()
    place_map = {"countryA": {"city1", "city2"}, "countryB": {"city2", "city3"}}

    # verbose with dict.get
    if (new_place := place_map.get("countryC")) is None:
        place_map["countryC"] = new_place = set()
        new_place.add("city5")

    # terse with setdefault
    country_d = place_map.setdefault("countryD", set())
    country_d.add("city6")

    print(place_map)

    _cr()


def _use_defaultdict_for_internal_state():
    _div()

    class Places:
        def __init__(self):
            self.data = defaultdict(set)

        def add(self, country, city):
            self.data[country].add(city)

    places = Places()
    print(f"places: {places}")
    places.add("country a", "city1")
    print(f"places: {places}")


if __name__ == "__main__":
    _terse_setdefault_vs_long_get()
    _use_defaultdict_for_internal_state()
