import requests
import json

class Janrain:
    def __init__(self, rootDomain, api_key):
        self.janrainDomain = "https://%s.rpxnow.com" % rootDomain

    def janrainRequest(*args):
        

    class EngageClient:
        """This client enables you to interact with Janrain's Engage API."""
        pass

    class CaptureClient:
        """This client enables you to interact with Janrain's Capture REST API."""
    
        def clientAdd(client_id, client_secret, description):
            if client_id and client_secret and description:
                if type(client_id) == str and type(client_secret) == str and type (description) == str:
                    add_client_dir = janrainDoman + "/clients/add"
                    add_client_payload = json.dumps()
                    add_client_response = requests.post(add_client_dir, data=add_client_payload)
                    return add_client_response
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

    class FederateClient:
        """This client enables you to interact with Janrain's Federate API."""
        pass