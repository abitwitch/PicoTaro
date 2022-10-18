from machine import Pin
import utime
import epaper

led = Pin(25, Pin.OUT)

epd = epaper.EPD_2in9_B()
#epd.flip()
epd.imageblack.fill(0xff)
epd.imagered.fill(0xff)
epd.imageblack.text("Hello world", 0, 10, 0x00)
epd.imagered.text("Hello world", 0, 20, 0x00)
epd.display()




def flash(on,off):
    led.high()
    utime.sleep(on)
    led.low()
    utime.sleep(off)



