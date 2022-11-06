# PicoTaro

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
7) Navigate to this repo. Upload the "deck" folder and all files in it, "envrandom.py", "epaper.py", and "main.py"


## Next features
 - Make images flippable (reverses)
 - Text helper in black ink
 - Text helper only for unlabled or reversed cards
 - Shuffling screen has suffle icon
 - Shuffling screen in inverted black ink
 - Shuffling screen has helper text about env random
 - Add moon phases
 - Add capacity to invert black and white (dark mode or reverse)
 - Use `import _thread' to shuffle while shuffle screen is loading
