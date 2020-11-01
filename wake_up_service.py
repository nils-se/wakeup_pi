## this small script reads a wakeup time (start_time) and dims up an Govee LED.
## start_time: LED goes on at minimum brightness and keeps on getting brighter
## dimmer_time: till start_time+dimmer_time the LED keeps getting brighter and reaches its maximum brightness at this point
## end_time: at this time the LED shuts off

## deutsch:
## Kleines Skript, das eine Datei ausliest und die Weckzeit daraus zieht.
## Innerhalb der Weckzeit dimmt die Lampe dann hoch und bleibt für eine
## gewisse Zeit an.



# The bulb seems to have a white-mode which uses cold/warm white LEDs instead of the RGB LEDs.
# Supply a value between -1 (warm) and 1 (cold)



import time
import subprocess
from govee_btled import BluetoothLED

from datetime import datetime

start_time = "0800"
end_time = "0900"

dimmer_time = 30*60 ## dimmer_time in minutes * 60 (for seconds)
print("starting program, wakup at ", start_time)

counter = 0
brightness = 0
led_on = 0

while(1):
    counter += 1
    print("counter: ", counter)
## read file


## get current time

    time.sleep(15)
    now = datetime.now()
    print(now)

    current_time = now.strftime("%H%M")
    print("Current Time =", current_time)

    subprocess.call("killall gatttool", shell=True)


    if current_time >= start_time and current_time < end_time:
        print("switching on LED")
        while(led_on == 0):
            try:
                print("starting to try to activate LED")
                led = BluetoothLED('***THE MAC-adress OF YOUR LED***')
                led.set_state(True)
                led.set_color_white(-1)
                led_on = 1
                print("led_on = 1")
            except:
                print("can't activate LED")
                subprocess.call("killall gatttool", shell=True)
                print("killed all gatttool")
                time.sleep(3)

        i = 1
        multi = 4
        while i < 100*multi:

            try:
                led.set_brightness(i/(200*multi))
                print("brightness: ",i/(200*multi))
                #led.set_color_white(-(100-i)/100)
                time.sleep(dimmer_time/(200*multi))
                i += 1
                brightness += 2/(200*multi)
            except:
                print("error in while #1 try")
                subprocess.call("killall gatttool", shell=True)
                time.sleep(5)
                led = BluetoothLED('***THE MAC-adress OF YOUR LED***')
                led.set_state(True)
                time.sleep(2)

            print(i)


        i = 1

        while i < 100*multi:

            try:
                led.set_brightness(i/(200*multi) + 0.5)
                led.set_color_white(-1+i/(50*multi))
                time.sleep(dimmer_time/(200*multi))
                i += 1
                brightness += 2/(200*multi)
            except:
                print("error in while #2 try")
                subprocess.call("killall gatttool", shell=True)
                time.sleep(5)
                led = BluetoothLED('***THE MAC-adress OF YOUR LED***')
                led.set_state(True)
                time.sleep(2)

            print(i)

        while(current_time < end_time):
            now = datetime.now()
            print(now)
            time.sleep(15)

            current_time = now.strftime("%H%M")
            print("sleeping till the end")
            print("Current Time =", current_time)



    if counter == 4:
        print("entering turn off")
        counter = 0
        subprocess.call(["/usr/bin/python3", "/home/pi/turn_off_led.py"])
  
