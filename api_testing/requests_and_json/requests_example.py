import pprint
import requests


rq = requests.get("https://api.spacexdata.com/v3/capsules")

print(rq.status_code)
print(rq.headers)
print(rq.encoding)
print(rq.text)
pprint.pprint(rq.json())

