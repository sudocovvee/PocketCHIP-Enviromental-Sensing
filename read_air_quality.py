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
        dat = [bus.read_byte_data(address, 2), bus.read_byte_data(address, 3)]
    return dat


# dht11 Sensor Read

#Print the data:
dat = alg_result_data()
print(dat)
