# PicoTaro
A disconnected digital taro deck. 

## Images
The images were sourced from [openclipart.org](https://openclipart.org/artist/klaatu-tarot). The original illustrations are by Pamela Colman Smith, 1910 from the Rider–Waite–Smith Tarot deck. 

## Hardware
This project uses: 
 - [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
 - [Waveshare 2.66inch E-Paper E-Ink Display (B)](https://www.waveshare.com/pico-epaper-2.66-b.htm)

## Setup
1) Download and install Thonny `sudo apt install thonny`
2) Open Thonny with `sudo thonny`
3) Download and install Circuit Python onto the pico, by going [here](https://circuitpython.org/board/raspberry_pi_pico/) and installing the latest stable release
4) Connect the Pico while holding BOOTSEL and copy over the UFC file. Restart the Pico
5) In Thonny select "Run > Select Interpreter > CircuitPython (generic)"
6) Prepare to upload files ("View" > "Files")
7) Navigate to this repo. Upload the "deck" and "fullmoons" folders and all files in them, "envrandom.py", "epaper.py", "main.py", "moonclock.py", "moongraphic.py", and "pcf8563.py"

## Next features
 - Move config from main to separate file (and add to README setup above)
 - Shuffling screen has suffle icon
 - Add capacity to invert black and white (dark mode or reverse)
