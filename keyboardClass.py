from pynput import keyboard

global TEST
TEST = False

class Keyboard():
    
    def __init__(self, targetKey = "]"):

        self.targetKey = targetKey
        self.pressedKey = ""

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
        except:
            if key == keyboard.Key.esc:
                quit()

    def on_release(self, key):
        self.pressedKey = ""
        if TEST:
            print("{} was released".format(key))

if __name__ == "__main__":

    myKeyboard = Keyboard()
    print(myKeyboard.getTargetKey())
    listener = keyboard.Listener(
    on_press= myKeyboard.on_press,
    on_release = myKeyboard.on_release)
    listener.start()
