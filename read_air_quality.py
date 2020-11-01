#import time
from smbus2 import SMBus
# This needs to be the Pocketchip vesion
# import RPi.GPIO as GPIO
#import CHIP_IO.GPIO as GPIO

address = 0x5a

# initialize GPIO
#GPIO.setup("CSID0", GPIO.OUT)

def alg_result_data():
    with SMBus(2) as bus:
        eCO2 = bus.read_byte_data(address, 2) + (bus.read_byte_data(address, 2) << 1)
        VOC = (bus.read_byte_data(address, 2) << 2) + (bus.read_byte_data(address, 2) << 3)
        final_dat = ("eCO2: "+ str(eCO2) + "\nVOC: " + str(VOC)) # + dat2
    return final_dat


def status():
    with SMBus(2) as bus:
        dat1 = bus.read_byte_data(address, 0)
        final_dat = str(dat1 << 7)
    return final_dat


# dht11 Sensor Read

#Print the data:
dat1 = alg_result_data()
dat2 = status()
print("Status: " + dat2 + "\nData: " + dat1)
