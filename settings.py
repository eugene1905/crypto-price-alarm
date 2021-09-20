import json


def init():
    global coins, transport_fees, service_charge, cost, exchg_rate, cnt, mode, target
    with open('config.json', 'r') as f:
        config = json.load(f)

    coins = ['BTC', 'ETH', 'XRP', 'LTC', 'BCH']
    transport_fees = {'bl': {'BTC': 0.0005, 'ETH': 0.008, 'XRP': 0.25,
                             'LTC': 0.001, 'BCH': 0.0001},  # transfer fee from binance to luno
                      'lb': {'BTC': 0.0003, 'ETH': 0.01, 'XRP': 0.25,
                             'LTC': 0.001, 'BCH': 0.0001}}  # transfer fee from luno to binance
    service_charge = {'luno': 0.005, 'binance': 0.004}
    cost = {}
    for i in coins:
        cost[i] = config[i]
    exchg_rate = config['exchg']
    mode = config['mode']
    target = config['target']
    cnt = 0
