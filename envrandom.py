from machine import ADC
import utime
import random

sensor_temp = ADC(4)

def envRandomInt(start, stop, sampleTimeMs):
    startTime=utime.ticks_ms()
    seed=1
    while utime.ticks_diff(utime.ticks_ms(), startTime) < sampleTimeMs:
        seed = sensor_temp.read_u16() + utime.ticks_us()
        random.seed(seed)
        seed = random.randint(start, stop)
    return(random.randint(start, stop))


if __name__=="__main__":
    sampleTimeMs=10
    sampleCount=500
    start=0
    stop=50
    log=[0]*(stop-start+1)
    print(f"Generating histogram for randomness. Estimated wait time: {sampleTimeMs*sampleCount/1000} seconds")
    while sum(log) < sampleCount:
        log[envRandomInt(start, stop, sampleTimeMs)]+=1    
    for count in log:
        print("."*count)