import random
import json
from config import *


def load_stock_list():
    with open(stock_list_json) as f:
        data = json.load(f)
    return data


def select_one_ranom_stock():
    return random.choice(load_stock_list())


def stock_selector(stock_list=[], random_size=25):
    """
    Return an ordered list of random stocks
    """
    pass
