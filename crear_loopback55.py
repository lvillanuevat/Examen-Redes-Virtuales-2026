import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

router_ip = "192.168.43.200"
username = "admin"
password = "Admin123"

url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=Loopback55"
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback55",
        "description": "Loopback55 creada por script Python del grupo",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.55.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

response = requests.put(
    url,
    auth=(username, password),
    headers=headers,
    data=json.dumps(payload),
    verify=False,
)

print("Codigo de estado:", response.status_code)
print("Respuesta:")
print(response.text)
