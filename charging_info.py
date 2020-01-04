import commands
import keychain
from teslapy import Tesla


with Tesla(commands.ACCOUNT, keychain.get_password(commands.SERVICE, commands.ACCOUNT),
           commands.CLIENT_ID, commands.CLIENT_SECRET) as tesla:
    tesla.fetch_token()
    cars = tesla.vehicle_list()
    selected = [c for c in cars if c['id_s'] == '4870041930736488']
    if len(selected) != 1:
        raise ValueError("one and only one car must be selected")
    for i, vehicle in enumerate(selected):
        vehicle.sync_wake_up()
        ch = vehicle.get_vehicle_data()['charge_state']
        print(f"""Charging State: {ch['charging_state']} 
Time To Full Charge: {ch['time_to_full_charge']:02.0f}:{(60*ch['time_to_full_charge']%60):02.0f}""")
        print(f"""Battery Level: {str(ch['battery_level']) + '%':23}
Battery Range: {vehicle.dist_units(ch['battery_range'])}""")
        print(f"""Charge Energy Added: {str(ch['charge_energy_added']) + ' kWh':17}
Charge Range Added: {vehicle.dist_units(ch['charge_miles_added_rated'])}""")
