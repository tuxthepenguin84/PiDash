#!/bin/bash
cd /home/pi/projects/PiDash/python
python3 main.py
xdotool search --desktop 0 --onlyvisible --name "Pi Dashboard" windowactivate --sync key --clearmodifiers ctrl+r