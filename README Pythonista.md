# TeslaPy

A Python implementation based on [unofficial documentation](https://tesla-api.timdorr.com/) of the client side interface to the Tesla Motors Owner API, which provides functionality to monitor and control Tesla vehicles remotely.

## Pythonista
Using Pythonista 3 you will be able to put the Python scripts to good use on iOS.
You'll need Pythonista 3 for this: http://omz-software.com/pythonista/. 
I have no ties with omz-software, I am just a user.

## Scripts
The following scripts are defined at this moment:
* charge_port_close.py
* charge_port_open.py
* charging_info.py
* climate_off.py
* climate_on.py
* trunk_front.py
* trunk_rear.py

## Setup
To make the environment ready on iOS for the above scripts, you'll need to run setup_keychain.py first, after setting your information in commands.py:

 `# CHANGE THIS`
 `ACCOUNT="richard.kooijman@inergy.nl"`
 `SERVICE="TeslaPy"`
 `VEHICLE_ID='XXXXXXXXXX'`

Furthermore, when you run this setup script, it will ask you for your password to put it into your keychain. I suggest you checkout the setup_keychain.py for security reasons.

From this moment on, the scripts will use your credentials as stored in the keychain to communicate with your Tesla.
