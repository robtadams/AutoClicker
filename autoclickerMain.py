import tkinter as tk
from keyboardClass import Keyboard
from mouseClass import Mouse

global TEST
TEST = False

class clickerApp():
    def __init__(self, window):

        # Window configuration
        window.rowconfigure([0,1,2], pad = 10, weight = 1)
        window.columnconfigure([0, 1], pad = 25, weight = 1)

        # Test stuff
        if TEST:
            label00 = tk.Label(master = window, background = "light gray")
            label00.grid(row = 0, column = 0, sticky = "nesw")

            label11 = tk.Label(master = window, background = "light gray")
            label11.grid(row = 1, column = 1, sticky = "nesw")

            label20 = tk.Label(master = window, background = "light gray")
            label20.grid(row = 2, column = 0, sticky = "nesw")

        # Variables
        self.key = "F6"
        self.targetKeyBool = False
        self.clickRate = 1000
        self.targetPosition = [-1, -1]
        self.currentPosition = [-1, -1]
        self.myMouse = Mouse()
        self.myKeyboard = Keyboard()
        self.myKeyboard.listen()

        # keyButton
        self.keyButton = tk.Button(master=window, text="Key", command = self.setTargetKey)
        self.keyButton.grid(row = 0, column = 0, sticky = "nesw", padx = 50, pady = 10)

        # keyEntry
        self.keyEntry = tk.Entry(master = window, text = "F6")
        self.keyEntry.grid(row = 0, column = 1)
        self.keyEntry.insert(0, self.key)

        # rateLabel
        self.rateLabel = tk.Label(master = window, text = "Click Rate (ms)")
        self.rateLabel.grid(row = 1, column = 0, pady = 10)

        # rateEntry
        self.clickRate = 1000
        self.rateEntry = tk.Entry()
        self.rateEntry.grid(row = 1, column = 1)
        self.rateEntry.insert(0, self.clickRate)

        # positionLabel
        self.positionLabel = tk.Label(master = window, text = "Mouse Position")
        self.positionLabel.grid(row = 2, column = 0, pady = 10)

        # positionFrame
        self.positionFrame = tk.Frame(
            master = window,
            relief = tk.FLAT,
            borderwidth = 1
        )
        self.positionFrame.grid(row = 2, column = 1)

        # xEntry
        self.xEntry = tk.Entry(master = self.positionFrame)
        self.xEntry.grid(row = 0, column = 0, padx = 10)
        if self.targetPosition[0] > 0:
            self.xEntry.insert(0, self.position[0])

        # yEntry
        self.yEntry = tk.Entry(master = self.positionFrame)
        self.yEntry.grid(row = 0, column = 1, padx = 10)
        if self.targetPosition[1] > 0:
            self.yEntry.insert(0, self.position[1])
    
    def setTargetKey(self):
        return

window = tk.Tk()
clickerApp(window)

window.mainloop()

