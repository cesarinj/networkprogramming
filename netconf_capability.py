from ncclient import manager

ios_xe = {
             "address": "192.168.56.103",
             "port": 830,
             "username": "cisco",
             "password": "cisco123!"
          }
if __name__ == '__main__':
    with manager.connect(   host=ios_xe["address"],
                            port=ios_xe["port"],
                            username=ios_xe["username"],
                            password=ios_xe["password"],
                            hostkey_verify=False ) as m:
        print ("Capability")
        for capability in m.server_capabilities:
            print (capability)