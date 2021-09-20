import data
import settings
import time
from datetime import datetime


def getBLMsg():
    msg = f"========================================== {settings.cnt} {settings.exchg_rate} ==============================================="
    msg += "\n[Luno Price(RM)]"
    for i in settings.coins:
        if i == 'XRP':
            tmp = "%.4f" % round(data.luno[0][i], 4)
        else:
            tmp = "%.2f" % round(data.luno[0][i], 2)
        msg += f"\t{i}:{tmp}"

    msg += "\n[Binance Price(USDT)]"
    for i in settings.coins:
        if i == 'XRP':
            tmp = "%.4f" % round(data.binance[0][i], 4)
        else:
            tmp = "%.2f" % round(data.binance[0][i], 2)
        msg += f"\t{i}:{tmp}"

    msg += "\n[Profit Rate(%)]"
    for i in settings.coins:
        tmp = "%.3f" % round(data.profit_rate[0][i], 3)
        msg += f"\t{i}:{tmp}"

    msg += "\n[Est. Gain(RM)]\t"
    for i in settings.coins:
        tmp = "%.2f" % round(data.profit[0][i], 2)
        msg += f"\t{i}:{tmp}"

    msg += "\n[Suggestion]\t"
    for i in settings.coins:
        tmp = round(settings.cost[i]+settings.transport_fees['bl'][i], 7)
        msg += f"\t{i}:{tmp}"
    msg += '\n==================================================================================================='
    return msg


def getLBMsg():
    msg = f"========================================= {settings.cnt} Reverse {settings.exchg_rate} ==========================================="
    msg += "\n[Luno Price(RM)]"
    for i in settings.coins:
        if i == 'XRP':
            tmp = "%.4f" % round(data.luno[1][i], 4)
        else:
            tmp = "%.2f" % round(data.luno[1][i], 2)
        msg += f"\t{i}:{tmp}"

    msg += "\n[Binance Price(USDT)"
    for i in settings.coins:
        if i == 'XRP':
            tmp = "%.4f" % round(data.binance[1][i], 4)
        else:
            tmp = "%.2f" % round(data.binance[1][i], 2)
        msg += f"\t{i}:{tmp}"

    msg += "\n[Profit Rate(%)]"
    for i in settings.coins:
        tmp = "%.3f" % round(data.profit_rate[1][i], 3)
        msg += f"\t{i}:{tmp}"

    msg += "\n[Est. Gain]\t"
    for i in settings.coins:
        tmp = "%.2f" % round(data.profit[1][i], 2)
        msg += f"\t{i}:{tmp}"

    msg += "\n[Suggestion]\t"
    for i in settings.coins:
        tmp = round(settings.cost[i]+settings.transport_fees['lb'][i], 7)
        msg += f"\t{i}:{tmp}"

    msg += '\n====================================================================================================='
    return msg


def getBLLog():
    now = datetime.now()
    log = f"{now}"
    for i in settings.coins:
        log += f",{data.luno[0][i]}"
    for i in settings.coins:
        log += f",{data.binance[0][i]}"
    for i in settings.coins:
        log += f",{data.profit_rate[0][i]}"
    for i in settings.coins:
        log += f",{data.profit[0][i]}"
    log += ",bl\n"
    return log


def getLBLog():
    now = datetime.now()
    log = f"{now}"
    for i in settings.coins:
        log += f",{data.luno[1][i]}"
    for i in settings.coins:
        log += f",{data.binance[1][i]}"
    for i in settings.coins:
        log += f",{data.profit_rate[1][i]}"
    for i in settings.coins:
        log += f",{data.profit[1][i]}"
    log += ",lb\n"
    return log
