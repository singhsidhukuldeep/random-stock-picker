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


def select_list_of_ranom_stock(data=""):
    return random.sample(load_stock_list(data), config.random_stocks_sampled)
