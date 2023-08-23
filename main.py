import ntc_templates
from netmiko import ConnectHandler
from Network.Devices import Switches
from csv import writer
from rich import print as rp

'''
Backing up Running-configurations
'''
filepath = input('Backup location: ')
for swiches in Switches.values():
    conn = ConnectHandler(**swiches)
    conn.enable()
    host = conn.send_command('show version',use_textfsm=True)[0]['hostname']
    output = conn.send_command('show run')

    rp(f'Backing up {host} running Configurations\n,{("-"*50)}')

    with open(f'{filepath}/{host}','w') as f:
        f.write(output)
    conn.disconnect()

    



