import mouse

"""
Mouse class
This is a class that defines the controller for the mouse
It will click on the targetPos, iff that position is greater than -1

"""

class Mouse():
    def __init__(self, clickRate = 1000, targetPos = [-1, -1]):
        
        self.clickRate = clickRate
        self.targetPos = targetPos

    def setClickRate(self, clickRate):
        self.clickRate = clickRate

    def setTargetPos(self, targetPos):
        self.targetPos = targetPos

    def getPos(self):
        return mouse.get_position()

    def click(self):
        try:

            # Move mouse X
            if self.targetPos[0] >= 0:
                mouse.move(self.targetPos[0], self.getPos()[1], absolute = True)

            # Move mouse Y
            if self.targetPos[1] >= 0:
                mouse.move(self.getPos()[0], self.targetPos[1], absolute = True)

            mouse.click("left")
        except:
            return False

if __name__ == "__main__":
    myMouse = Mouse(targetPos = [100, 100])
    myMouse.click()
    print(myMouse.getPos())
