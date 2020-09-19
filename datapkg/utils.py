import json
import sys

from constants import COIN_ATTRIBS
from crypto_compare_api import coin_list
from crypto_compare_api import live_price

def collect_coin_data(filename):
    data = coin_list()
    gathered_dict = {}
    for key in data.keys():
        temp_data = data[key]
        gathered_dict[key] = {}
        for item in COIN_ATTRIBS:
            gathered_dict[key][item] = temp_data[item]
        print gathered_dict[key]

    with open(filename, 'w') as coin_json:
        json.dump(gathered_dict, coin_json, indent=4)

def read_json(filename):
    with open(filename, 'r') as file_ptr:
        data = json.load(file_ptr)
    return data

def ret_exchange_list(exchange_list):
    valid_exchange_list = list()
    for item in exchange_list:
        print item
        try:
            data = live_price('XRP', ['USD'], item)
            if 'Message' in data.keys() and "market does not exist" in data['Message']:
                continue
            else:
                print data
                valid_exchange_list.append(item)
        except KeyError:
            print KeyError
            sys.exit(1)

    return valid_exchange_list


def validate_result(result):
    if 'Message' in result.keys() and "market does not exist" in result['Message']:
        print("this combination does not exist")
        return False
    else:
        return True