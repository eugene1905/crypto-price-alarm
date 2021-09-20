import settings
import data
import time
import msg
import menu
import keyboard
import winsound


keep_going = True


def init():
    settings.init()
    data.init()


def refreshData():
    data.getBinanceOrder()
    data.getLunoOrder()
    data.getBLData()
    data.getLBData()


def alertMe():
    winsound.Beep(2500, 1000)


init()
f1 = open("bl_info.txt", "at")
f2 = open("lb_info.txt", "at")
while keep_going:
    refreshData()
    settings.cnt += 1
    if settings.mode == 'bl':
        Message = msg.getBLMsg()
    else:
        Message = msg.getLBMsg()
    for i in settings.coins:
        if data.profit_rate[0][i] > settings.target:
            alertMe()
        if data.profit_rate[1][i] > settings.target:
            alertMe()
    print(Message)
    if settings.cnt % 60 == 1:
        f1.write(msg.getBLLog())
        f2.write(msg.getLBLog())
    if keyboard.is_pressed("ctrl+shift"):  # actions
        keep_going = menu.Configurate()
    time.sleep(1)
f1.close()
f2.close()
