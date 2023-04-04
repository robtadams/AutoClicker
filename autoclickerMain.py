import tkinter as tk
import threading
from pynput import keyboard
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

        # Keyboard variables
        self.targetKey = "*"
        self.targetKeyPressed = False

        # Mouse variables
        self.clickRate = 1000
        self.targetPosition = [-1, -1]
        self.currentPosition = [-1, -1]

        # Class construction
        self.myMouse = Mouse()
        self.myKeyboard = Keyboard(self.targetKeyPressed, targetKey = self.targetKey)

        # Key listener thread
        listener = keyboard.Listener(
        on_press = self.myKeyboard.on_press,
        on_release = self.myKeyboard.on_release)
        
        listener.start()

        # keyButton
        self.keyButton = tk.Button(master=window, text="Key", command = self.setTargetKey)
        self.keyButton.grid(row = 0, column = 0, sticky = "nesw", padx = 50, pady = 10)

        # keyEntry
        self.keyEntry = tk.Entry(master = window, text = self.targetKey)
        self.keyEntry.grid(row = 0, column = 1)
        self.keyEntry.insert(0, self.targetKey)

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

    def getTargetKeyPressed(self):

        return self.targetKeyPressed
    
    def setTargetKey(self):

        self.keyEntry.delete(0, tk.END)
        self.keyEntry.insert(0, "Please enter a key....")
        
        while self.myKeyboard.getPressedKey() == "":
            pass
        self.targetKey = self.myKeyboard.getPressedKey()
        self.myKeyboard.setTargetKey(self.targetKey)

        self.keyEntry.delete(0, tk.END)
        self.keyEntry.insert(0, self.targetKey)

def threadFunction(targetKeyPressed):
    var = True
    while True:
        print(targetKeyPressed)
    
window = tk.Tk()
app = clickerApp(window)
x = threading.Thread(target = threadFunction, args=(app.getTargetKeyPressed(), ))
x.start()

