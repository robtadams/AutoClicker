import tkinter as tk
import threading
import mouse
import time
from pynput import keyboard

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
        global targetKey
        targetKey = "*"
        global targetKeyPressed
        targetKeyPressed = False
        global clickRate
        clickRate = 1000
        global targetPosition
        targetPosition = [-1, -1]

        # Keyboard listener thread
        listener = keyboard.Listener(
        on_press = self.on_press,
        on_release = self.on_release)
        
        listener.start()

        # Mouse controller thread
        controller = threading.Thread(
            target = self.clickLoop,
            args = ())
        controller.start()

        # keyButton
        global setTargetKey
        setTargetKey = False
        self.keyButton = tk.Button(master=window, text="Key", command = self.setTargetKey)
        self.keyButton.grid(row = 0, column = 0, sticky = "nesw", padx = 50, pady = 10)

        # keyEntry
        self.keyEntry = tk.Entry(master = window, text = "*")
        self.keyEntry.grid(row = 0, column = 1)
        self.keyEntry.insert(0, "*")

        # rateButton
        self.rateLabel = tk.Button(master = window, text = "Click Rate (ms)", command = self.setClickRate)
        self.rateLabel.grid(row = 1, column = 0, pady = 10)

        # rateEntry
        self.rateEntry = tk.Entry()
        self.rateEntry.grid(row = 1, column = 1)
        self.rateEntry.insert(0, clickRate)

        # positionLabel
        self.positionButton = tk.Button(master = window, text = "Mouse Position", command = self.setTargetPosition)
        self.positionButton.grid(row = 2, column = 0, pady = 10)

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

        # yEntry
        self.yEntry = tk.Entry(master = self.positionFrame)
        self.yEntry.grid(row = 0, column = 1, padx = 10)

    def on_press(self, key):

        if TEST:
            print("{} was pressed".format(key))

        global targetKey

        try:
            if key.char == targetKey:
                if TEST:
                    print("Target key was pressed...")
                global targetKeyPressed
                targetKeyPressed = not targetKeyPressed

        except:
            if key == keyboard.Key.esc:
                quit()

    def on_release(self, key):

        if TEST:
            print("{} was released".format(key))

    def clickLoop(self):

        clickBool = True
        
        while True:
                
            if targetKeyPressed:

                if clickBool:
                    
                    clickBool = False
                    print("Starting...")

                if int(targetPosition[0]) >= 0:
                    print("Moving mouse X to {}".format(targetPosition[0]))

                if int(targetPosition[1]) >= 0:
                    print("Moving mouse Y to {}".format(targetPosition[1]))

                mouse.move(targetPosition[0], targetPosition[1], absolute = True)
                
                print("Click!")
                mouse.click()
                time.sleep(clickRate / 1000)

            elif not clickBool:

                clickBool = True
                print("Stopping...")

    def handle_keypress(self, event):

        global setTargetKey
        if setTargetKey:

            global targetKey
            self.keyEntry.delete(0, tk.END)
            self.keyEntry.insert(0, event.char)
            setTargetKey = False

            try:

                
                targetKey = event.char

            except:

                targetKey = "*"

            print(targetKey)

    def setTargetKey(self):

        self.keyEntry.delete(0, tk.END)
        self.keyEntry.insert(0, "Please enter a key...")
        global setTargetKey
        setTargetKey = True

    def setClickRate(self):

        global clickRate
        try:

            clickRate = int(self.rateEntry.get())
            print("{}ms click rate...".format(clickRate))

        except:

            clickRate = 1000

    def setTargetPosition(self):

        xPos = self.xEntry.get()
        yPos = self.yEntry.get()
        
        if xPos == "":
            xPos = -1

        if yPos == "":
            yPos = -1

        print("xPos: {0}\nyPos: {1}".format(xPos, yPos))

        global targetPosition
        targetPosition = [xPos, yPos]
        

window = tk.Tk()
app = clickerApp(window)
window.bind("<Key>", app.handle_keypress)
