import csv
from datetime import datetime, timedelta
import json
import os.path
import sys
from io import StringIO

import requests

base_url = "https://parliamentuk.pdswebops.org"
route_source = "https://raw.githubusercontent.com/ukparliament/ontologies/master/urls.csv"

def retrieve_route_list():
    links_response = requests.get(route_source)
    io = StringIO(links_response.text, newline='')
    reader = csv.reader(io, delimiter=',')
    return (
        {
            'path': route,
            'description': line[2],
            'type': line[3]
        }
        for line in reader
        for route in replace_resource_id(line[1])
        if line[0] != '' and line[1] != 'Route'
    )

with open(os.path.join(os.path.dirname(__file__), 'resource_map.json')) as resource_map_file:
    resource_map = json.load(resource_map_file)

def replace_resource_id(route):
    for id in resource_map:
        route = route.replace(id, resource_map[id])
    alphabet = (chr(c) for c in range(ord('a'), ord('z') + 1))
    if ':letters' in route:
        yield from [route.replace(':letters', c) for c in alphabet]
    else:
        yield route

def record_route_status(routes):
    ix = 0
    total = len(routes)
    start_time = datetime.utcnow()
    for route in routes:
        ix += 1
        item_time = datetime.utcnow()
        path = route['path']
        url = base_url + route['path']
        sys.stdout.write('{0} of {1}: {2}'.format(ix, total, url))
        sys.stdout.flush()
        req = requests.get(url, allow_redirects=False)
        finish_time = datetime.utcnow()
        elapsed = finish_time - item_time
        total_elapsed = finish_time - start_time
        print(' {0} - {1}s ({2}s)'.format(
            req.status_code,
            round(elapsed.total_seconds(), 1),
            round(total_elapsed.total_seconds(), 1),
        ))

def main():
    route_array = list(retrieve_route_list())
    record_route_status(route_array)

if __name__ == '__main__':
    main()
