### Identifica en que equipos estan los trasceiver 

from netmiko import ConnectHandler
switch_hp= {  "SW01" : "10.10.10.10",
          }
switch_aruba= { "SW02" : "10.10.10.11",
            }
switch_cisco= { "SW03" : "10.10.10.12",  # 
                "SW04" : "10.10.10.13",  # 
                "SW05" : "10.10.10.16",   
                "SW06" : "10.10.10.14", 
                "SW07" : "10.10.10.15", 
                }
trasceiver_sn = ["ACW22120209","AGJ2206R307"]
for z in switch_cisco :
    sshCli = ConnectHandler(
        device_type='cisco_ios',
        host=switch_cisco[z], 
        port=22, 
        username='cisco', 
        password='cisco123.'
        )
    comando ="sh inventory "
    output = sshCli.send_command(comando)
    for sn in trasceiver_sn:    
        with open('modulo.txt', 'a') as f: 
            if sn in output:
                salida=z+' '+switch_cisco[z]+' '+sn
                print (salida)
                f.write(salida+'\n') 
print("Finished")


