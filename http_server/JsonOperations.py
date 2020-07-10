class Payload(object):
    def __init__(self, action, method, data):
        self.action = action
        self.method = method
        self.data = data

message = {"action":"print","method":"onData","data":"Madan Mohan"}
import json

def as_payload(dct):
    return Payload(dct['action'], dct['method'], dct['data'])

payload = json.loads(message, object_hook = as_payload)