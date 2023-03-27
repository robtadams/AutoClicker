from pynput import keyboard

class Keyboard():
    
    def __init__(self, targetKey = "F6"):

        self.targetKey = targetKey
        self.keyPressed = False

    def setTargetKey(self, targetKey):

        self.targetKey = targetKey

    def getTargetKey(self):

        return self.targetKey

    def handleHotkey(self):
        self.keyPressed = not self.keyPressed
        print(self.keyPressed)

    def on_press(self, key):
        print("{} was pressed".format(key))
        try:
            if key.char == self.targetKey:
                print("Target key was pressed...")
        except:
            return

if __name__ == "__main__":

    myKeyboard = Keyboard()
    print(myKeyboard.getTargetKey())
    listener = keyboard.Listener(
    on_press= myKeyboard.on_press)
    listener.start()
