
from Network.Devices import Switches
from netmiko import ConnectHandler
from fastapi import FastAPI
import ntc_templates

app = FastAPI()


'''
Show VLANS configured on Switches
'''
@app.get('/Devices/Switches/{Switch_name}/GET/VLANs')
def vlans(Switch_name: str):
    switch = Switches[Switch_name]
    conn   = ConnectHandler(**switch)
    conn.enable()

    command = conn.send_command('show vlan brief',use_textfsm=True)
    return {f'{Switch_name}': command} 


'''
Verifying Spanning tree status on Switches
'''
@app.get('/Devices/Switches/{Switch_name}/GET/Spanningtree/{VLAN_ID}/status')
def vlans(Switch_name: str, VLAN_ID: str):
    switch = Switches[Switch_name]
    conn   = ConnectHandler(**switch)
    conn.enable()

    command = conn.send_command('show spanning-tree '+VLAN_ID,use_textfsm=True)
    return {f'{Switch_name}': command} 


'''
Verifying Etherchannels on Switches
'''
@app.get('/Devices/Switches/{Switch_name}/GET/Etherchannel')
def vlans(Switch_name: str):
    switch = Switches[Switch_name]
    conn   = ConnectHandler(**switch)
    conn.enable()

    command = conn.send_command('show etherchannel summary',use_textfsm=True)
    return {f'{Switch_name}': command} 



'''
Verifying MAC-Address tables on Switches
'''
@app.get('/Devices/Switches/{Switch_name}/GET/addresstable/{VLAN_ID}')
def vlans(Switch_name: str, VLAN_ID:str):
    switch = Switches[Switch_name]
    conn   = ConnectHandler(**switch)
    conn.enable()

    command = conn.send_command('show mac address-table '+VLAN_ID,use_textfsm=True)
    return {f'{Switch_name}': command} 