import json
import requests

host = 'https://55.15.67.46'
auth = ("admin", "zdns")
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'}
params = {'current_user': 'admin'}
data = json.dumps(params)

url = (host + ":" + "20120" + '/views/default/zones')
print("url: " + url)

response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
print("%s" % response.json())