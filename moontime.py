import pcf8563
from machine import Pin
import time


i2c=machine.I2C(0, sda=Pin(8), scl=Pin(9))

clk=pcf8563.PCF8563(i2c)

#Set time (should only be run with plugged into computer)
#clk.set_datetime(time.localtime())

century=21 #todo store century in disabled alarm

print(clk.datetime())

def epochtime():
    now=dict(zip(["year", "month", "date", "day", "hours", "minutes", "seconds"],clk.datetime()))
    
    now["year"]=int(str(century-1)+str(now["year"]))
    now["yearday"]=123 #TODO
    
    x=(now["year"], now["month"], now["date"], now["hours"], now["minutes"], now["seconds"], now["day"], now["yearday"])
    print(time.mktime(x))
    epoch=(1970, 1, 1, 3, 0, 0, 0)
    epoch=dict(zip(["year", "month", "date", "day", "hours", "minutes", "seconds"],epoch))
    epochtime=(now["year"]-epoch["year"])
    
    
    #TODO timezone

print(time.time())
epochtime()

with open("log.txt", "a") as f:
    f.write("\ntime: "+str(time.time()))



