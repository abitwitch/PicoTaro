import pcf8563
import machine
import time
from fullmoons import fullmoons

class clock:
    def __init__(self, sda=16, scl=1):
        self.i2c=machine.I2C(0, sda=machine.Pin(sda), scl=machine.Pin(scl))
        self.rtc=pcf8563.PCF8563(self.i2c)
        self.fullmoons=fullmoons.fullmoons()
    
    def set_clock(self, utcOffsetHours):
        now=list(time.localtime(time.time()-(utcOffsetHours*60*60)))
        now=now[:-1]
        now[6]+=1 #clock day runs 1-7, not 0-6
        self.rtc.set_datetime(now)
        #store century
        m=int(str(now[0])[0])
        c=int(str(now[0])[1])
        self.rtc.set_daily_alarm(m,c)
        self.rtc.turn_alarm_off()

    def time(self):
        now=dict(zip(["year", "month", "date", "day", "hour", "minute", "second"],self.rtc.datetime()))
        m=self.rtc.get_daily_alarm()[0]
        c=self.rtc.get_daily_alarm()[1]
        now["year"]=(m*1000)+(c*100)+now["year"]
        now["yearday"]=None
        nowTuple=(now["year"], now["month"], now["date"], now["hour"], now["minute"], now["second"], now["day"], now["yearday"])
        return(time.mktime(nowTuple))
    
    def moon(self):
        #this function runs at O(n) but could be re-factored to O(log(n)) if nessesary using binary search
        time=self.time()
        synodicMonth=29.530588861*60*60*24
        prevFullMoon,nextFullMoon=self.fullmoons.getCurrentMoonRange(time)
        if prevFullMoon==None:
            cycles=int((nextFullMoon-time)/synodicMonth)
            prevFullMoon=nextFullMoon-(synodicMonth*(cycles+1))
            nextFullMoon=nextFullMoon-(synodicMonth*(cycles+0))
        elif nextFullMoon==None:
            cycles=int((time-prevFullMoon)/synodicMonth)
            nextFullMoon=prevFullMoon+(synodicMonth*(cycles+1))
            prevFullMoon=prevFullMoon+(synodicMonth*(cycles+1))
        phase=(time-prevFullMoon)/(nextFullMoon-prevFullMoon)
        phase=(phase+0.5)%1
        return(phase)            

if __name__ == "__main__":
    clk=clock()
    utcOffsetHours=-5 #set manually
    #comment in to set clock (should only be run with plugged into computer)
    #clk.set_clock(utcOffsetHours)
    print(f"Currrent time on Pico's clock: {str(clk.time())}")
    print(f"  (year, month, mday, hour, minute, second, weekday, yearday): {str(clk.rtc.datetime())}")
    print(f"  Moonphase (0-1): {str(clk.moon())}")

