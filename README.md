# PicoTaro
A disconnected digital taro deck. 

## Images
The images were sourced from [openclipart.org](https://openclipart.org/artist/klaatu-tarot). The original illustrations are by Pamela Colman Smith, 1910 from the Rider–Waite–Smith Tarot deck. 

## Hardware
This project uses: 
 - [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
 - [Waveshare 2.66inch E-Paper E-Ink Display (B)](https://www.waveshare.com/pico-epaper-2.66-b.htm)
 - [Waveshare PCF8563 RTC Board](https://www.waveshare.com/pcf8563-rtc-board.htm)

## Hardware build
1) Insure the RTC is connected in battery ("BAT") mode
2) Connect RTC to the Pico
    - VCC on RTC to Pin 36 on Pico
    - GND on RTC to any ground Pin on Pico
    - SDA on RTC to Pin 21 on Pico
    - SCL on RTC to Pin 2 on Pico
3) Plug the Pico into the E-Paper Display

## Setup
1) Download and install Thonny `sudo apt install thonny`
2) Open Thonny with `sudo thonny`
3) Install MicroPython for the Pico by using the language selector at the bottom left of the thonny window
4) Prepare to upload files ("View" > "Files")
5) Navigate to this repo. Upload the "deck" and "fullmoons" folders and all files in them, "envrandom.py", "epaper.py", "main.py", "moonclock.py", "moongraphic.py", and "pcf8563.py"
6) To set the clock on the pico
    1) Open `moonclock.py` and comment in the line `clk.set_clock(utcOffsetHours)`
    2) Change the `utcOffsetHours=-5` to your current timezone

## Next features
 - Move config from main to separate file (and add to README setup above)
 - Shuffling screen has suffle icon
 - Add capacity to invert black and white (dark mode or reverse)
 - Idea: manually set reverse, not reverse with a boot while two pins are connected
 - Add welcome / instructions page on first load
