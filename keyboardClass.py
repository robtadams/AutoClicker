from pynput import keyboard

global TEST
TEST = True

class Keyboard():
    
    def __init__(self, targetKeyPressed, targetKey = "]"):

        self.targetKey = targetKey
        self.pressedKey = ""
        self.targetKeyPressed = targetKeyPressed

    def setTargetKey(self, targetKey):

        self.targetKey = targetKey

    def getTargetKey(self):

        return self.targetKey

    def getPressedKey(self):

        return self.pressedKey

    def on_press(self, key):
        if TEST:
            print("{} was pressed".format(key))
        try:
            self.pressedKey = key.char
            if key.char == self.targetKey:
                print("Target key was pressed...")
                self.targetKeyPressed = True
        except:
            if key == keyboard.Key.esc:
                quit()

    def on_release(self, key):
        self.pressedKey = ""
        if TEST:
            print("{} was released".format(key))
