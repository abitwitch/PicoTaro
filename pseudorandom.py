from machine import ADC
import utime
import random

sensor_temp = ADC(4)

def dots(v):
    v-=15
    v*=10
    v*=2
    print("."*int(v))

'''
while True:
    print(sensor_temp.read_u16())
    utime.sleep(0.1)
'''
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
 
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    dots(temperature)
    #print("Temperature: {}".format(temperature))
    utime.sleep(0.1)
    
    