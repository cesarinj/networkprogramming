from ncclient import manager
import xml.dom.minidom
import xmltodict
import xml.dom.minidom

# create a variable object that represents the NETCONF session
m = manager.connect(
         host="192.168.56.103",
         port=830,
         username="cisco",
         password="cisco123!",
         hostkey_verify=False
         )

print (m.connected)
running_config = m.get_config('running')
running_config_beautify=xml.dom.minidom.parseString(str(running_config)).toprettyxml()
running_config_txt=str(running_config)
with open("running.xml","w") as file:
    file.write(running_config_txt) 

with open("running_beautify.xml","w") as file:
    file.write(running_config_beautify)  


print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())
m.close_session()