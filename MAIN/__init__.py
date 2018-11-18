from MAIN import arduinoSerial
from tkinter import *
'''
@Author Frank Ricker
'''
def setupSerial():
	global arduino
	arduino=arduinoSerial.Arduino(9600,'*',0)
def disconnect():
	arduino.closePort()
	print('Port closed !!!')
setupSerial()
class myGUI():
    def __int__(self, master):
        global arduino
        self.master = master
        self.text = ""
        master.title("Bridge Controler")
        self.openButton = Button(master, text= "Open", command = self.open).pack()
        self.closeButton = Button(master, text= "Close", command = self.close).pack()
    def open(self):
        global arduino
        print("Opening")
        arduino.serWrite("4")
    def close(self):
        global arduino
        print("Closeing")
        arduino.serWrite("5")
root = Tk()
myGUI = myGUI(root)
root.mainloop()


