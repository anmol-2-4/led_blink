# 😀 led_blink

yo this is just a blink sketch lol. nothing crazy, just an LED turning on and off forever. did it two ways cause why not - one in C++ (the normal arduino way) and one in MicroPython.

## what it actually does

LED goes on for half a second, off for half a second, repeat forever. classic "hello world" of hardware basically. the python version is a lil extra and blinks the board's built-in LED AND an external one at the same time.

## files in here

- `sketch/sketch.ino` - the arduino sketch, blinks pin 12
- `sketch/sketch.yaml` - build config for the sketch (using arduino:zephyr platform)
- `python/main.py` - micropython version, blinks `D13` (built-in led) + `D11` (external led) together
- `app.yaml` - just metadata for the app (name, icon, etc)

## wiring

- built-in led: do nothing, its already on the board lol
- external led: hook one up on `D11` to ground, dont forget a resistor or you'll fry it

## how to run

open it up in arduino cloud editor (or just the regular arduino IDE if you only want the .ino part) and smash the run/upload button. thats it, ur done
