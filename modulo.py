### Identifica en que equipos estan los trasceiver 

from netmiko import ConnectHandler

switch_3com= {  "SWCONTDC" : "10.100.100.113",
          }
switch_3com1= { "SW3PCTAL" : "10.100.100.132",

            }
switch_cisco= { "SWBRCSHM" : "10.100.100.121",  # Recurss humanos  9300
                "SW33DIDT" : "10.100.100.124",  # JQUIROZ  9300
 #               "SW1PRLPB" : "10.100.100.126",   #cat 9300 Relaciones publicas 
                "SW1PCPMT" : "10.100.100.134", #ok Laboratorio Cómputo 9
                "SW3PLB42" : "10.100.100.135", # ws WS-C3560-24PS-E
                }
    
trasceiver_sn = ["ACW22120BC9","AGJ2206R6L7"]
#print(switch_ip["SWCONTDC"])

for z in switch_cisco :
  #  print(z)
  #  print(switch_cisco[z])
    sshCli = ConnectHandler(
        device_type='cisco_ios',
        host=switch_cisco[z], 
        port=22, 
        username='AdminSwitch', 
        password='1n1ct3l2020.'
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


