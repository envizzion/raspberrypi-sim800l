from sms import SMS
import RPi.GPIO as logging

class SmsTrigger:
    PORT="/dev/serial0"
    BAUD=9600

    def init(self,ser):
        
        s=SMS(PORT,BAUD,loglevel=logging.DEBUG)
        s.setup()
        if not s.turnOn(): exit(1)
        if not s.setEchoOff(): exit(1)
        print("SIM800 module initalized succesfully!")

    def setTelephoneNumber(self,tpNumber):
           self.phoneNumber = tpNumber

