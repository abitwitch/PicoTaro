from machine import Pin
import utime
import epaper

led = Pin(25, Pin.OUT)


epd = epaper.EPD_2in9_B()

epd.flip()
epd.imageblack.fill(0xff)
epd.imagered.fill(0xff)

deck=['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'M00', 'M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10', 'P11', 'P12', 'P13', 'P14', 'S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S12', 'S13', 'S14', 'W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W08', 'W09', 'W10', 'W11', 'W12', 'W13', 'W14']

cardModule=deck[0]


card=__import__(f"deck.{cardModule}", None, None, [None])

epd.buffer_black=card.img

txt=card.name
txt_pos_x=max(0,76-int(len(txt)*8/2))
txt_pos_y=276
epd.imagered.text(txt, txt_pos_x, txt_pos_y, 0x00)
epd.display()



def flash(on,off):
    led.high()
    utime.sleep(on)
    led.low()
    utime.sleep(off)





