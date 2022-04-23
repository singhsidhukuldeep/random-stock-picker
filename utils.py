from operator import imod
import random
import json
from functools import lru_cache
import configurations as config

@lru_cache(maxsize=len(config.stock_exchanges))
def load_stock_list(stock_list_json):
    with open(stock_list_json) as f:
        data = json.load(f)
    return data


def select_one_ranom_stock(data=""):
    return random.choice(load_stock_list(data))
