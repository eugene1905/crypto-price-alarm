import settings
import threading
import requests

'''**********************************************
; Get orderbooks through api(s) via GET request
**********************************************'''


def init():
    global luno_order, binance_order, profit, profit_rate, luno, binance
    profit = [{}, {}]
    profit_rate = [{}, {}]
    luno_order = {}
    binance_order = {}
    luno = [{}, {}]
    binance = [{}, {}]


def getLunoRequest(coin):
    url = f'https://api.mybitx.com/api/1/orderbook_top?pair={coin}MYR'
    coin = 'BTC' if coin == 'XBT' else coin
    luno_order[coin] = {'asks': [], 'bids': []}
    r = requests.get(url)
    x = r.json()
    x.pop('timestamp')
    res = []
    for i in x['asks']:
        lst = [float(i['price']), float(i['volume'])]
        res.append(lst)
    luno_order[coin]['asks'] = res
    res = []
    for i in x['bids']:
        lst = [float(i['price']), float(i['volume'])]
        res.append(lst)
    luno_order[coin]['bids'] = res


def getBinanceRequest(coin):
    url = f'https://api.binance.com/api/v3/depth?symbol={coin}USDT&limit=50'
    binance_order[coin] = {'asks': [], 'bids': []}
    r = requests.get(url)
    x = r.json()
    x.pop('lastUpdateId')
    res = []
    for i in x['asks']:
        lst = [float(i[0]), float(i[1])]
        res.append(lst)
    binance_order[coin]['asks'] = res
    res = []
    for i in x['bids']:
        lst = [float(i[0]), float(i[1])]
        res.append(lst)
    binance_order[coin]['bids'] = res


def getLunoOrder():
    global luno_order
    luno_order = {}
    threads = []
    for i in settings.coins:
        i = 'XBT' if i == 'BTC' else i
        x = threading.Thread(target=getLunoRequest, args=(i,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()
    return luno_order


def getBinanceOrder():
    global binance_order
    binance_order = {}
    threads = []
    for i in settings.coins:
        x = threading.Thread(target=getBinanceRequest, args=(i,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()
    return binance_order


'''**********************************************
; Data Processing
**********************************************'''


def getAvg(orderbook, _cost):
    res = 0
    for i in orderbook:  # i: {price, volume}
        res += i[0] * min(i[1], _cost)
        _cost -= i[1]
        if(_cost <= 0):
            break
    return res


# Binance to Luno
def getBLData():
    global luno, binance, profit, profit_rate
    for i in settings.coins:
        luno_avg = getAvg(luno_order[i]['bids'], settings.cost[i])
        luno[0][i] = luno_avg / settings.cost[i]
        binance_avg = getAvg(
            binance_order[i]['asks'], settings.cost[i]+settings.transport_fees['bl'][i])
        binance[0][i] = getAvg(binance_order[i]['asks'],
                               settings.cost[i]) / settings.cost[i]
        profit[0][i] = luno_avg*(1-settings.service_charge['luno']) - \
            binance_avg * \
            (1+settings.service_charge['binance'])*settings.exchg_rate
        profit_rate[0][i] = profit[0][i] / \
            binance_avg / settings.exchg_rate * 100

# Luno to Binance


def getLBData():
    global luno, binance, profit, profit_rate
    for i in settings.coins:
        binance_avg = getAvg(binance_order[i]['bids'], settings.cost[i])
        binance[1][i] = binance_avg / settings.cost[i]
        luno_avg = getAvg(luno_order[i]['asks'],
                          settings.cost[i]+settings.transport_fees['lb'][i])
        luno[1][i] = getAvg(luno_order[i]['asks'],
                            settings.cost[i]) / settings.cost[i]
        profit[1][i] = binance_avg*(1-settings.service_charge['binance'])*settings.exchg_rate - \
            luno_avg*(1+settings.service_charge['luno'])
        profit_rate[1][i] = profit[1][i] / luno_avg * 100
