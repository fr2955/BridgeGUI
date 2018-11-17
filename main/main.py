import serial
serial = serial.Serial('COM5',9600)
class bridgeGet():
    def __init__(self, master):
        self.state = 0
        self.read = null
        self.read = serial.read()
    def getState(self):
        if serial.inWaiting()
            self.state = serial.readline()
            print("The self.state is "+self.state)
            if(self.state = 0)
               print("The bridge is closed")
            if(self.state = 1)
                print("The bridge is oppen")
            if(self.state = 2)
                print("The bridge is opening")
            if(self.state = 3)
                print("The birdge is clossing")


