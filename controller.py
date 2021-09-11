import os


ADDRESS = os.popen("bluetoothctl paired-devices").read()[7:24].replace(":", "_")

BT_CONNECTION = "dbus-send --system --print-reply --dest=org.bluez /org/bluez/hci0/dev_"+ADDRESS+" org.bluez."

def connection(command):
    return os.popen(BT_CONNECTION+command).read()


