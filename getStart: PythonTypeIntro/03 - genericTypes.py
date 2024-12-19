# You can use the same builtin types as generics (with square brackets and types inside):

# * list
# * tuple
# * set
# * dict

# And the same as with Python 3.8, from the typing module:

# Union
# Optional (the same as with Python 3.8)
# ...and others.

# In Python 3.10, as an alternative to using the generics "Union" and "Optional",
#  you can use the vertical bar (|) to declare unions of types, that's a lot better and simpler.
# From Python 3.8-
#from typing import List

#def process_items(items: List[str]):
#   for item in items:
#       print(item)
#


# From python 3.9+
def process_items(items: list[str]):
    for item in items:
        print(item)

# from python 3.8-
# from typing import Set, Tuple

# def process_items_more(items_t: Tuple[int, int, str], items_s: Set[bytes]):
#    return items_t, items_s

# From Python 3.9+
def process_items_more(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


# From Python 3.8-
# from typing import Dict


# def process_items_more_more(prices: Dict[str, float]):
#    for item_name, item_price in prices.items():
#        print(item_name)
#        print(item_price)


# From Python 3.9+
def process_items_more_more(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


# From python 3.8-
# from typing import Union

# def process_item_more_more_more(item: Union[int, str]):
#     print(item)

# From Python 3.10+
def process_item_(item: int | str):
    print(item)


# From python 3.8+
# from typing import Optional

# def say_hi(name: Optional[str] = None):
#   if name is not None:
#       print(f"Hey {name}!")
#   else:
#       print("Hello World")


# From Python 3.10+
def say_hi_1(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

# From Python 3.8-
# from typing import Optional

# def say_hi(name: Optional[str]):
#     print(f"Hey {name}!")

# Python 3.10+
def say_hi_2(name: str | None):
        print(f"Hey {name}!")

say_hi_2(name = None)
say_hi_2("Ali")

# From Python 3.8-
# from typing import Optional

# def say_hi_(name: Optional[str]):
#     print(f"Hey {name}!")

# From Python 3.10+
def say_hi(name: str | None):
    print(f"Hey {name}!")
