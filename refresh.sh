#!/bin/bash
xdotool search --desktop 0 --onlyvisible --name "pi@raspberrypi" windowactivate
xdotool search --desktop 0 --onlyvisible --name "pi@raspberrypi" windowmove 1261 658
cd /home/pi/projects/PiDash/python
python3 main.py
2>/dev/null 1>&2 xdotool search --desktop 0 --onlyvisible --name "Pi Dashboard" windowactivate --sync key --clearmodifiers alt+Home
xdotool mousemove 1919 1079