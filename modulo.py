### Identifica en que equipos estan los trasceiver 

from netmiko import ConnectHandler

switch_3com= {  "SWCONTDC" : "10.10.10.10",
          }
switch_3com1= { "SW3PCTAL" : "10.10.10.11",

            }
switch_cisco= { "SWBRCSHM" : "10.10.10.12",  # Recurss humanos  9300
                "SW33DIDT" : "10.10.10.13",  # JQUIROZ  9300
 #               "SW1PRLPB" : "10.100.100.126",   #cat 9300 Relaciones publicas 
                "SW1PCPMT" : "10.10.10.14", #ok Laboratorio Cómputo 9
                "SW3PLB42" : "10.10.10.15", # ws WS-C3560-24PS-E
                }
    
trasceiver_sn = ["ACW22120209","AGJ2206R307"]
#print(switch_ip["SWCONTDC"])

for z in switch_cisco :
  #  print(z)
  #  print(switch_cisco[z])
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


