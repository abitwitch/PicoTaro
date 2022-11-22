import utime
import epaper
import envrandom
import machine
import zlib
import moonclock
import moongraphic
import _thread

deck=['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'M00', 'M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10', 'P11', 'P12', 'P13', 'P14', 'S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S12', 'S13', 'S14', 'W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W08', 'W09', 'W10', 'W11', 'W12', 'W13', 'W14']

epd = epaper.EPD_2in9_B()
epd.flip()
clock=moonclock.clock()
led = machine.Pin(25, Pin.OUT)

def flash(on,off):
    led.high()
    utime.sleep(on)
    led.low()
    utime.sleep(off)
    
def showShuffleScreen():
    epd.imageblack.fill(0xff)
    epd.imagered.fill(0xff)
    txt="shuffling..."
    txt_pos_x = max(0,76-int(len(txt)*8/2))
    txt_pos_y = 148
    epd.imageblack.text(txt, txt_pos_x, txt_pos_y, 0x00)
    txt_pos_x = max(0,76-int(len(txt)*8/2))
    txt_pos_y = 148
    epd.imagered.text(txt, txt_pos_x, txt_pos_y, 0x00)
    epd.display()

def shuffle():
    return(envrandom.envRandomInt(0,len(deck)-1,10000))

def drawCard(cardIndex):
    card = __import__(f"deck.{deck[cardIndex]}", None, None, [None])
    return(card)

def loadCardToScreen(card):
    epd.imageblack.fill(0xff)
    epd.imagered.fill(0xff)
    epd.buffer_black = bytearray(zlib.decompress(card.img_zip))

def loadMoonphaseGraphicToScreen():
    epd.buffer_black=epd.buffer_black[0:len(epd.buffer_black)-len(moongraphic.image)]+bytearray(moongraphic.image)

def getMoonphase():
    return(clock.moon())

def loadMoonphaseMarkerToScreen(moonphase):
    screenWidth=152
    screenHeight=296
    markerWindowStart=8
    markerWindowHeight=int(len(moongraphic.image)*8/screenWidth)
    markerWindowEnd=screenWidth-markerWindowStart
    markerWindowWidth=markerWindowEnd-markerWindowStart
    marker2=round(moonphase*markerWindowWidth)
    marker1=round(moonphase*markerWindowWidth)+1
    marker3=round(moonphase*markerWindowWidth)-1
    marker1=(marker1%markerWindowWidth)+markerWindowStart
    marker2=(marker2%markerWindowWidth)+markerWindowStart
    marker3=(marker3%markerWindowWidth)+markerWindowStart
    epd.imagered.vline(marker1, screenHeight-markerWindowHeight, markerWindowHeight, 0x00)
    epd.imagered.vline(marker2, screenHeight-markerWindowHeight, markerWindowHeight, 0x00)
    epd.imagered.vline(marker3, screenHeight-markerWindowHeight, markerWindowHeight, 0x00)


if __name__ == "__main__":
    _thread.start_new_thread(showShuffleScreen, ())
    cardIndex=shuffle()
    card=drawCard(cardIndex)
    epd.reset()
    loadCardToScreen(card)
    loadMoonphaseGraphicToScreen()
    moonphase=getMoonphase()
    loadMoonphaseMarkerToScreen(moonphase)
    epd.display()
    flash(0.5,0.5)
    flash(0.5,0.5)
    flash(0.5,0.5)

