import random
import json


def load_stock_list(stock_list_json):
    with open(stock_list_json) as f:
        data = json.load(f)
    return data


def select_one_ranom_stock(data=""):
    return random.choice(load_stock_list(data))


def stock_selector(stock_list=[], random_size=25):
    """
    Return an ordered list of random stocks
    """
    pass
