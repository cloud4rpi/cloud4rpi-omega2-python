Cloud4RPi Examples for [Onion Omega2](https://onion.io/omega2/)
=========================================================================================================================

[![Build Status](https://travis-ci.org/cloud4rpi/cloud4rpi-omega2-python.svg?branch=master)](https://travis-ci.org/cloud4rpi/cloud4rpi-omega2-python)

## Running the Sample Code

1. Update your system and make sure you have the latest versions of all required software:
    ```sh
    oupgrade
    opkg update
    opkg install wget python python-pip
    pip install --upgrade setuptools pip
    ```
2. Install the Cloud4RPi client library:
    ```sh
    pip install cloud4rpi
    ```
3. Download examples:
    ```sh
    mkdir cloud4rpi-omega2-python && cd cloud4rpi-omega2-python
    repo="https://raw.githubusercontent.com/cloud4rpi/cloud4rpi-omega2-python/master"
    wget $repo"/omega2.py" $repo"/led.py" $repo"/rgb_led.py"
    ```

    > You can install **git** if your board has sufficient memory and you prefer using it, and clone this repository with the `opkg install git git-http ca-bundle && git clone https://github.com/cloud4rpi/cloud4rpi-omega2-python.git && cd cloud4rpi-omega2-python` command.

4. [Log into your Cloud4RPi account](https://cloud4rpi.io/auth) or [create a new one](https://cloud4rpi.io/auth/signup).
5. Copy [your device](https://cloud4rpi.io/devices)'s **Device Token**. If you have no devices, create one on the [Devices](https://cloud4rpi.io/devices) page and copy its **Device Token**.
6. Replace the `__YOUR_DEVICE_TOKEN__` string in the [led.py](https://github.com/cloud4rpi/cloud4rpi-omega2-python/blob/master/led.py) file with your device token using any text editor (**vim**, **sed** or other):
    ```sh
    sed -i 's/__YOUR_DEVICE_TOKEN__/replace-this-text-with-your-real-device-token/' led.py
    ```
7. Run the `led.py` example:
    ```sh
    python led.py
    ```
8. Notice that the [device](https://cloud4rpi.io/devices) went online and started sending data.
9. Go to the [Control Panels](https://cloud4rpi.io/control-panels/) page and add a new control panel.
10. Add a new **Switch** widget and bind it to the `Omega LED` variable.

You can use this control panel to switch the [onboard LED](https://docs.onion.io/omega2-docs/the-omega-led.html)'s state.

![](https://github.com/cloud4rpi/docs/raw/master/example-img/omega_led.png)

> If you have an [Expansion Dock](https://docs.onion.io/omega2-docs/expansion-dock.html), run the `rgb_led.py` example to control the dock's RGB LED.

## See Also

* [Examples for Raspberry Pi](https://github.com/cloud4rpi/cloud4rpi-raspberrypi-python)
* [Examples for Next Thing Co. C.H.I.P.](https://github.com/cloud4rpi/cloud4rpi-chip-python)
* [Client Library](https://github.com/cloud4rpi/cloud4rpi)
* [Documentation Repository](https://github.com/cloud4rpi/docs)
