import json
import requests
requests.packages.urllib3.disable_warnings()
api_url= "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }
baiscauth = ("cisco", "cisco123!")
resp = requests.get(api_url, auth=baiscauth, headers=headers, verify=False)
print(resp)
response_json = resp.json()
print(response_json)
print(json.dumps(response_json, indent=4))