import settings
import equations
import time
import tkinter as tk
from threading import Thread

INTERVAL = 1


class MainPanel:
    def __init__(self):
        pass

    def start(self):
        self.root = tk.Tk()
        self.root.geometry('1000x1000')
        self.root.title('Penny')
        self.add_button = tk.Button(self.root, text="Monitor", font=(
            None, 12), command=self.add_monitor).pack(pady=40)
        self.root.mainloop()

    def add_monitor(self):
        self.monitor = tk.Tk()
        self.monitor.title('Monitor')
        self.monitor.geometry('1000x1000')
        self.profit = [{}, {}]
        self.label = [{}, {}]
        for i in settings.coins:
            self.profit[0][i] = tk.StringVar()
            self.label[0][i] = tk.Label(
                self.monitor, textvariable=self.profit[0][i]).pack()
            self.profit[1][i] = tk.StringVar()
            self.label[1][i] = tk.Label(
                self.monitor, textvariable=self.profit[1][i]).pack()

        while True:
            self.update_data()
            time.sleep(INTERVAL)

    def update_data(self):
        settings.refreshData()
        for i in settings.coins:
            self.profit[0][i].set(settings.profit[0][i])
            self.profit[1][i].set(settings.profit[1][i])


settings.init()
gui = MainPanel()
gui.start()
