from ncclient import manager
import xml.dom.minidom
# create a variable object that represents the NETCONF session
m = manager.connect(
         host="192.168.56.103", 
         port=830,
         username="cisco",
         password="cisco123!",
         hostkey_verify=False
         )
netconf_data = """
<config><native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>R1</hostname>
</native></config>"""

netconf_reply = m.edit_config(target="running", config=netconf_data)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
 
#input("###### Press Enter to continue to Step 3 ######")

# create a new NETCONF config dataset
# it starts with the <config> element
# and inside includes the actual YANG config data
# It defines a Loopback 100 with 100.100.100.100/24

netconf_data = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>100</name>
    <description>TEST100</description>
    <ip>
     <address>
      <primary>
       <address>100.10.12.100</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

netconf_data3 = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>R1</hostname>
     <ip>
      <route>
          <ip-route-interface-forwarding-list>
               <prefix>192.168.10.0</prefix>
               <mask>255.255.255.0</mask>
               <fwd-list>
                    <fwd>192.168.56.5</fwd>
               </fwd-list>
           </ip-route-interface-forwarding-list>
      </route>


     </ip>
</native>
</config>"""

netconf_data4 = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback100</name>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>11.11.11.1</ip>
          <subnet>255.255.255.0</subnet>
        </address>
      </ipv6>

      <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>2001:1::3</ip>
          <prefix-length>64</prefix-length>
        </address>
      </ipv6>
    </interface>
  </interfaces>
</config>
"""


# to edit the config, use the edit_config() method
# target config and source NETCONF dataset
# print the output (should include <ok/>)
netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
netconf_reply = m.edit_config(target="running", config=netconf_data4)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



