import time
import subprocess
from govee_btled import BluetoothLED

print("turn off LED")

led = BluetoothLED('***THE MAC-adress OF YOUR LED***')
led.set_state(True)
led.set_brightness(0)

time.sleep (5)
subprocess.call("killall gatttool", shell=True)
