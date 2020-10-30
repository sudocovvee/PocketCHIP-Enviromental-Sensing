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
        dat1 = bus.read_byte_data(address, 2)
        dat2 = bus.read_byte_data(address, 3)
        final_dat = (dat1 << 8) + dat2
    return final_dat


def status():
    with SMBus(2) as bus:
        dat1 = bus.read_byte_data(address, 0)
        final_dat = str(dat1 << 8)
    return final_dat


# dht11 Sensor Read

#Print the data:
dat1 = alg_result_data()
dat2 = status()
print("Status: " + dat2 + "\nData: " + str(dat1))
