import os.path
import time
import RPi.GPIO as g

LED_R = 36
LED_Y = 38
LED_B = 40
BTN = 32

DEV_REG = '/sys/bus/i2c/devices/i2c-1/new_device'
DEV_REG_PARAM = 'sht21 0x40'
DEV_TMP = '/sys/class/hwmon/hwmon0/temp1_input'
DEV_HUM = '/sys/class/hwmon/hwmon0/humidity1_input'

g.setmode(g.BOARD)

g.setup(LED_R, g.OUT)
g.setup(LED_Y, g.OUT)
g.setup(LED_B, g.OUT)
g.setup(BTN, g.IN, pull_up_down=g.PUD_UP)

print('=== iC880A Backplane Test Program ===\n')

print('Turning on LEDs...')
g.output(LED_R, g.HIGH)
time.sleep(0.5)
g.output(LED_Y, g.HIGH)
time.sleep(0.5)
g.output(LED_B, g.HIGH)

print('\nWaiting for button...')
try:
    g.wait_for_edge(BTN, g.FALLING)
except KeyboardInterrupt:
    print('Aborted.')
    pass

g.output(LED_R, g.LOW)
g.output(LED_Y, g.LOW)
g.output(LED_B, g.LOW)

if input('\nTest sensor? [y/n]').strip() == 'y':
    print('Initializing sensor...')
    if os.path.isfile(DEV_TMP) and os.path.isfile(DEV_HUM):
        print('Already initialized.')
    with open(DEV_REG, 'wb') as f:
        f.write(DEV_REG_PARAM)
        print('Sensor registered.')
    print('Reading temperature... ', end='')
    with open(DEV_TMP, 'rb') as f:
        val = f.read().strip()
        temperature = float(int(val)) / 1000
        print(temperature)
    print('Reading humidity... ', end='')
    with open(DEV_HUM, 'rb') as f:
        val = f.read().strip()
        humidity = float(int(val)) / 1000
        print(humidity)


print('\n=== DONE! ===')

g.cleanup()
