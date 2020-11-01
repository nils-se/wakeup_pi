# wakeup_pi
Scripts for a controllable Wakeup Light build with a Raspberry Pi and a Govee LED

- Written for Raspberry Pi
- I am not a programmer. This is very messy code but it works every morning. You are nonetheless welcome to contribute to this code.

## requirements:
python3
govee_btled from Freemanium: https://github.com/Freemanium/govee_btled


## installation
0. update your pi, this prevents bluetooth issues
1. install the requirements from above and test if the LED ist reacting with the test script in the govee_btled repository
2. copy both files to your /home/pi/ directory
3. change all the MAC-Adresses in the scripts to the MAC-Adress of your Govee Bluetooth LED (how to find it: see below)
4. modify the start and end time for the wakeup time and test the script with "python3 wake_up_service.py"
5. add a systemd service for automatic startup  (see below)
6. add a restart at 2 or 3 o'clock in the night to prevent hangs in the bluetooth engine. It's a common problem of raspberry pis

## find MAC-adress of your LED
Use the command "bluetoothctl"
After firing it up tpye "scan on" and wait for a line like this one: 
>[NEW] Device XX:XX:XX:XX:XX:XX Minger_H6001_3E2C

Or another name like Govee. The identifier with lots of ":" is your MAC-adress


## systemd service for automatic start and restart in case the script hangs
1. sudo nano /etc/systemd/system/wake_up.service

add the following code:
```
[Unit]
Description=wake_up
Wants=graphical.target
After=graphical.target
Requires=bluetooth.target

[Service]
Type=simple
ExecStartPre=/usr/bin/xset -dpms
ExecStart=/usr/bin/python3 /home/pi/wake_up_service.py
Restart=always
RestartSec=20
User=pi
Group=pi

[Install]
WantedBy=graphical.target
```

2. sudo systemctl enable wake_up.service
