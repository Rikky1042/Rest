import requests
import json


URL ="http://127.0.0.1:8000/stucreate/"

data = {
    'name':'Ritesh',
   'roll':'675',
   'Class':'D',
   'School':'Mahavidyalaya',
   'mobile':78956489,

}

json_data=json.dumps(data)

r=requests.post(url=URL,data=json_data)

data= r.json()
print(data)