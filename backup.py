from netmiko import ConnectHandler

switch_aruba= { 
          }
switch_hp= { 
            }
switch_cisco= { "R1" : "192.168.56.103",  # ventas
            }
for z in switch_cisco :
    print(z)
    print(switch_cisco[z])
    sshCli = ConnectHandler(
        device_type='cisco_ios',
        host=switch_cisco[z], 
        port=22, 
        username='cisco', 
        password='cisco123!'
        )
    comando ="show run "
    print(comando)
    print(switch_cisco[z])
    showrun = sshCli.send_command(comando)
    path = "c:/backup/"+z+".cfg"
    file = open(path, "w")   # in append mode
    file.write(showrun)
    print("Pass  !!")