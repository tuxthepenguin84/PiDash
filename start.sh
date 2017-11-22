#!/bin/bash
chromium-browser --start-fullscreen &
cd /home/pi/projects/PiDash/python
while true
do
	python3 main.py
	sleep 60
done