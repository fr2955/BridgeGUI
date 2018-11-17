##import serial
class bridgeComuniocator():
    def __init__(self):
        self = self.Serial('COM5',9600)
        self.state = 0

