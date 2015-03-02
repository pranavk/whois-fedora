import json, requests, pprint

fas_name = requests.get('https://badges.fedoraproject.org/user/sadin/json')

output = fas_name.json()

pprint.pprint(output)
