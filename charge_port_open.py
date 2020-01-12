import commands
import keychain
from teslapy import Tesla


with Tesla(commands.ACCOUNT, keychain.get_password(commands.SERVICE, commands.ACCOUNT),
           commands.CLIENT_ID, commands.CLIENT_SECRET) as tesla:
    tesla.fetch_token()
    cars = tesla.vehicle_list()
    selected = [c for c in cars if c['id_s'] == keychain.get_password(commands.SERVICE, commands.VEHICLE_ID)]
    if len(selected) != 1:
        raise ValueError("one and only one car must be selected")
    for i, vehicle in enumerate(selected):
        vehicle.sync_wake_up()
        vehicle.command('CHARGE_PORT_DOOR_OPEN')
