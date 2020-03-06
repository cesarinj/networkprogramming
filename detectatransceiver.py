from netmiko import ConnectHandler
switch_aruba= { 
          }
switch_hp= { 
            }
switch_cisco= { "R1" : "192.168.56.103",  # ventas
            }
transceiver="ACW22120BC9"

with open("modulo.txt","r") as file:
    for linea in file:
        if transceiver in linea : 
            detecta=linea.find('SN:')
            print (linea[detecta:detecta+20])
