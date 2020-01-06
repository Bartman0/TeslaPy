""" Tesla Owner API CLI application using TeslaPy module """

# Author: Tim Dorssers

import argparse
from teslapy import Tesla

CLIENT_ID='e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e'
CLIENT_SECRET='c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220'

ACCOUNT="richard.kooijman@inergy.nl"
SERVICE="TeslaPy"
VEHICLE_ID='XXXXXXXXXX'


def main():
    parser = argparse.ArgumentParser(description='Tesla Owner API CLI')
    parser.add_argument('-e', dest='email', help='login email', required=True)
    parser.add_argument('-p', dest='password', help='prompt/specify login password', required=True)
    parser.add_argument('-i', '--id', help='select vehicle on id')
    parser.add_argument('-a', dest='api', help='API call endpoint name')
    parser.add_argument('-k', dest='keyvalue', help='API parameter (key=value)',
                        action='append', type=lambda kv: kv.split('=', 1))
    parser.add_argument('-c', dest='command', help='vehicle command endpoint')
    parser.add_argument('-l', '--list', action='store_true',
                        help='list all selected vehicles')
    parser.add_argument('-o', '--option', action='store_true',
                        help='list vehicle option codes')
    parser.add_argument('-v', '--vin', action='store_true',
                        help='vehicle identification number decode')
    parser.add_argument('-w', '--wake', action='store_true',
                        help='wake up selected vehicle(s)')
    parser.add_argument('-g', '--get', action='store_true',
                        help='get rollup of all vehicle data')
    parser.add_argument('-n', '--nearby', action='store_true',
                        help='list nearby charging sites')
    parser.add_argument('-m', '--mobile', action='store_true',
                        help='get mobile enabled state')
    parser.add_argument('-s', '--start', action='store_true',
                        help='remote start drive')
    parser.add_argument('-t', '--trunk', help='open trunk front/rear')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='set logging level to debug')
    args = parser.parse_args()
    with Tesla(args.email, args.password, CLIENT_ID, CLIENT_SECRET) as tesla:
        tesla.fetch_token()
        cars = tesla.vehicle_list()
        selected = [c for c in cars if c['id_s'] == args.id]
        if len(selected) != 1:
            raise ValueError("one and only one car must be selected")
        for i, vehicle in enumerate(selected):
            print('Vehicle %d:' % i)
            if args.list:
                print(vehicle)
            if args.option:
                print(', '.join(vehicle.option_code_list()))
            if args.vin:
                print(vehicle.decode_vin())
            if args.wake:
                vehicle.sync_wake_up()
            if args.get:
                print(vehicle.get_vehicle_data())
            if args.nearby:
                print(vehicle.get_nearby_charging_sites())
            if args.mobile:
                print(vehicle.mobile_enabled())
            if args.start:
                print(vehicle.remote_start_drive())
            if args.trunk:
                print(vehicle.command('ACTUATE_TRUNK', which_trunk=args.trunk))
            if args.api:
                data = dict(args.keyvalue) or {}
                print(vehicle.api(args.api, **data))

if __name__ == "__main__":
    main()
