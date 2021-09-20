import settings
import json


def Configurate():
    global current_mode
    with open('config.json', 'r') as f:
        config = json.load(f)

    cmd = "none"
    print("Console Menu:\nType \"q\" to quit, \"r\" to return, \"a\" to config everything, \"s\" to switch mode,\nor specifically \"target, exchange, BTC, ETH, XRP, LTC, BCH\"")
    while(cmd != "r"):
        cmd = input("$cmd> ")
        if(cmd == 'q'):
            return False
        editall = False if cmd != "a" else True
        if(cmd == 's'):
            config['mode'] = "bl" if settings.mode == "lb" else "lb"
        if(editall or cmd == "target"):
            config['target'] = float(input("[Target Profit Rate]: "))
        if(editall or cmd == "exchange"):
            config['exchg'] = float(input("[Exchange Ratio]: "))
        if(editall or cmd == "btc"):
            config['BTC'] = float(input("[BTC cost]: "))
        if(editall or cmd == "eth"):
            config['ETH'] = float(input("[ETH Cost]: "))
        if(editall or cmd == "xrp"):
            config['XRP'] = float(input("[XRP Cost]: "))
        if(editall or cmd == "ltc"):
            config['LTC'] = float(input("[LTC Cost]: "))
        if(editall or cmd == "bch"):
            config['BCH'] = float(input("[BCH Cost]: "))

    print("\n=================================================")
    print(";[Profit Target]: ", config['target'])
    print(";[Exchange Rate]: ", config['exchg'])
    print(";[BTC cost]: ", config['BTC'])
    print(";[ETH cost]: ", config['ETH'])
    print(";[XRP cost]: ", config['XRP'])
    print(";[LTC cost]: ", config['LTC'])
    print(";[BCH cost]: ", config['BCH'])
    print("=================================================")
    print()
    with open('config.json', 'w') as f:
        json.dump(config, f)
    settings.init()
    return True
