import requests
import json

class Janrain:
    def __init__(self, rootDomain):
        self.janrainDomain = "https://%s.rpxnow.com" % rootDomain
    
    def clientAdd(client_id, client_secret, description):
        if client_id and client_secret and description:
            if type(client_id) == str and type(client_secret) == str and type (description) == str:
                add_client_dir = janrainDoman + "/clients/add"
                add_client_payload = json.dumps()
                add_client_request = requests.post(add_client_dir, data=add_client_payload)
            else:
                raise TypeError("All input parameters for this function must be strings")
        else:
            raise TypeError("This request requires the parameters client_id, client_secret, and description")

    def clientWhitelist():
        pass

    def clientDelete():
        pass

    def clientsList():
        pass

    def clientSetDescription():
        pass

    def clientSetFeatures():
        pass

    def clientSetWhitelist():
        pass