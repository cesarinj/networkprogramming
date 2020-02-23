from netmiko import ConnectHandler

switch_3com= { 
          }
switch_3com1= { 
            }
switch_cisco= { "R1" : "10.10.10.10",  # ventas
                

for z in switch_cisco :
    print(z)
    print(switch_cisco[z])
    sshCli = ConnectHandler(
        device_type='cisco_ios',
        host=switch_cisco[z], 
        port=22, 
        username='cisco', 
        password='cisco.'
        )
    comando ="show run "
    print(comando)
    print(switch_cisco[z])
    showrun = sshCli.send_command(comando)
    path = "F:/TFTP/"+z+".cfg"
    file = open(path, "w")   # in append mode
    file.write(showrun)
    print("Pass")
    print("Finished")





