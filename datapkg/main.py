import matplotlib.pyplot as plt
import time
import json
from crypto_compare_api import live_price, minute_price_historical, coin_list
from constants import FULL_EXHANGE_LIST, WORK_ECHANGE_LIST, COIN_LIST_FILE
from utils import collect_coin_data, read_json, validate_result


does_not_exist = open('data_does_not_exit', 'w')


if __name__=="__main__":

    #while(1):
        # ret_exchange_list(['Bitstamp'])
    # with open('bitstamp2.txt', 'w') as btsf:
    #     btsf.write(minute_price_historical('BTC', 'USD', 100, 1, exchange='Bitstamp').to_string())
    # with open('coinbase2.txt', 'w') as cnbsf:
    #     cnbsf.write(minute_price_historical('BTC', 'USD', 100, 1, exchange='Coinbase').to_string())
    #     # data = [live_price('BTC', ['USD'], exchange='LiveCoin')]
    #     # print data
    #     #time.sleep(0.1)

    coin_basic_info = read_json(COIN_LIST_FILE)
    # collect data for each coin from possible exchanges
    for coin in coin_basic_info.keys():
        coin_basic_info[coin]['price_data'] = {}
        for exch in WORK_ECHANGE_LIST:
            print coin, exch
            try:
                temp = minute_price_historical(coin, 'USD', 100, 1, exchange=exch).to_string()
                coin_basic_info[coin]['price_data'][exch] = temp
            except Exception as general_exception:
                print("{}:{} combination does not exist".format(coin, exch))
                print(general_exception)
                does_not_exist.write("{}:{}\n".format(coin, exch))

    with open('final_coin_price_data.json', 'w') as target_file:
        json.dump(coin_basic_info, target_file, indent=4)
    does_not_exist.close()