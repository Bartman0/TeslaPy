import keychain
import commands
import getpass

keychain.set_password(commands.SERVICE, commands.ACCOUNT, getpass.getpass('Password: '))
keychain.set_password(commands.SERVICE, commands.VEHICLE_ID, '4870041930736488')
