from ncclient import manager
import xmltodict
ios_xe1 = {
             "address": "192.168.56.103",
             "port": 830,
             "username": "cisco",
             "password": "cisco123!"
          }
# NETCONF filter to use, in this case interfaceg1
netconf_filter = open("filter-ietf-interfaces.xml").read()

if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"],
                         port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        # Get Configuration and State Info for Interface
        netconf_reply = m.get(netconf_filter)

        # Process the XML and store in useful dictionaries
        intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        intf_config = intf_details["interfaces"]["interface"]
        intf_info = intf_details["interfaces-state"]["interface"]

        print("")
        print("Interface Details:")
        print("  Name: {}".format(intf_config["name"]))
        print("  Description: {}".format(intf_config["description"]))
        print("  Type: {}".format(intf_config["type"]["#text"]))
        print("  MAC Address: {}".format(intf_info["phys-address"]))
        print("  Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
        print("  Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))







# define a NETCONF filter to get only the required data
# w/o this filter the NETCONF GET operation will try to 
# return everything and will crash (aka. similar to 'debug all')
# the filter defines that we want to get only data defined
# in the ietf-interfaces model in the interfaces-state container

# use the xmldict module to parse the NETCONF reply (in xml form)
# the retuned object is a Python dictionary
netconf_reply_dict = xmltodict.parse(netconf_reply.xml)

# loop over the Python dictionary object and print the interesting data
for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
    print("Name: {} MAC: {} Input: {} Output {}".format(
                interface["name"],
                interface["phys-address"],
                interface["statistics"]["in-octets"],
                interface["statistics"]["out-octets"]
       )
