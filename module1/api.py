"""Testing web APIs with GET and POST"""

import json
import requests
import sys

osm = "https://nominatim.openstreetmap.org/search"
address = "Avenue Héger, Ixelles"
#address = sys.argv[1]
data = {'q': address, 'format': 'json'}
resp = requests.get(osm, data)
json_list = json.loads(resp.text)
for item in json_list:
    display_name = item['display_name']
    short_name = display_name.split(", ")[0]
    lat = item['lat']
    lon = item['lon']
    print(f"{short_name} ({lat} - {lon})")
