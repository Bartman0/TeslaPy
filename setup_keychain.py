import keychain
import commands
import getpass
from teslapy import Tesla

passwd = getpass.getpass('Password: ')
keychain.set_password(commands.SERVICE, commands.ACCOUNT, passwd)
keychain.set_password(commands.SERVICE, commands.VEHICLE_ID, commands.VEHICLE_ID)
with Tesla(commands.ACCOUNT, passwd,
           commands.CLIENT_ID, commands.CLIENT_SECRET) as tesla:
    tesla.fetch_token()
    cars = tesla.vehicle_list()
    print("vehicle ID: " + commands.VEHICLE_ID)
    print(cars)
    selected = [c for c in cars if c['id_s'] == keychain.get_password(commands.SERVICE, commands.VEHICLE_ID)]
    if len(selected) == 0:
        print("vehicle can not be found")
    elif len(selected) > 1:
        print("more than one vehicle found")
    else:
        print("everything seems to be set up OK")
