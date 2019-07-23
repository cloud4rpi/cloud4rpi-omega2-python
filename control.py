# -*- coding: utf-8 -*-
#
# Cloud4RPi Example for Omega2
# ============================
#
# This example demonstrates how to use Cloud4RPi service to control Omega2 LEDs.
#
# For complete instructions on how to run this example, refer
# to the [How To](https://cloud4rpi.github.io/docs/howto/) article.


from os import uname
from socket import gethostname
from time import sleep
import sys
import cloud4rpi
import omega2

# Put your device token here. To get the token,
# sign up at https://cloud4rpi.io and create a device.
DEVICE_TOKEN = '__YOUR_DEVICE_TOKEN__'

# Decrease this value for testing purposes.
DATA_SENDING_INTERVAL = 300  # seconds


class RGB_LED(object):
    def __init__(self, omega2_instance):
        self.o2 = omega2_instance
        self.R, self.G, self.B = 0, 0, 0

    def init(self):
        for _, pin in self.o2.RGB_pins.items():
            self.o2.gpio_dir_out_1(pin)  # HIGH = OFF

    def set_R(self, value):
        if value == self.R:
            return value
        self.R = value
        self.o2.RGB_color(self.R, self.G, self.B)
        return value

    def set_G(self, value):
        if value == self.G:
            return value
        self.G = value
        self.o2.RGB_color(self.R, self.G, self.B)
        return value

    def set_B(self, value):
        if value == self.B:
            return value
        self.B = value
        self.o2.RGB_color(self.R, self.G, self.B)
        return value


o2 = omega2.Omega2()
rgb = RGB_LED(o2)


def main():
    rgb.init()

    # Put variable declarations here
    variables = {
        'Omega LED': {
            'type': 'bool',
            'value': False,
            'bind': o2.led_control
        },
        'RGB LED - Red': {
            'type': 'numeric',
            'value': 0,
            'bind': rgb.set_R
        },
        'RGB LED - Green': {
            'type': 'numeric',
            'value': 0,
            'bind': rgb.set_G
        },
        'RGB LED - Blue': {
            'type': 'numeric',
            'value': 0,
            'bind': rgb.set_B
        }
    }

    # Put system data declarations here
    diagnostics = {
        'Host': gethostname(),
        'Operating System': " ".join(uname()),
        'Omega2 version': 'Omega2 Plus' if 'p' in o2.version else 'Omega2'
    }

    device = cloud4rpi.connect(DEVICE_TOKEN)
    device.declare(variables)
    device.declare_diag(diagnostics)

    device.publish_config()

    # Adds a 1 second delay to ensure device variables are created
    sleep(1)

    try:
        device.publish_diag()
        while True:
            device.publish_data()
            sleep(DATA_SENDING_INTERVAL)

    except KeyboardInterrupt:
        cloud4rpi.log.info('Keyboard interrupt received. Stopping...')
        sys.exit(0)

    except Exception as e:
        error = cloud4rpi.get_error_message(e)
        cloud4rpi.log.error("ERROR! %s %s", error, sys.exc_info()[0])
        sys.exit(1)


if __name__ == '__main__':
    main()
