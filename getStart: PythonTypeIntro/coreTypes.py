# Declaring Types
def get_items(name: str, age: int, gravity: float, onOFF: bool, bIT8: bytes):
    return name, age, gravity, onOFF, bIT8


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
