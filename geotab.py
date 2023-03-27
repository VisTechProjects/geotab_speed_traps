import mygeotab
import pprint
import datetime
with open(r'C:\Users\Vis\Documents\geotab_login.txt', 'r') as file:
    loginpw = file.read().rstrip()

api = mygeotab.API(username='vismantaskuznecovas@gmail.com',
                   password=loginpw, database='vis')
api.authenticate()

# result = api.get('Device', resultsLimit=2)
# result

result = api.get('Zone')
pprint.pprint(result[6])

datadict = {
    "name": "Example zone 123",
    "mustIdentifyStops": "true",
    "displayed": "true",
    "activeFrom": "1986-01-01T00:00:00.000Z",
    "activeTo": "2050-01-01T00:00:00.000Z",
    "zoneTypes": ["ZoneTypeOfficeId"],
    "fillColor": [{"r": "255", "g": "165", "b": "0", "a": "191"}],
    "points": [{"x": "-79.712318", "y": "43.438266"}, {"x": "-79.711181", "y": "43.437461"}, {"x": "-79.712677", "y": "43.436168"}, {"x": "-79.713966", "y": "43.437107"}, {"x": "-79.712318", "y": "43.438266"}],
    "groups": [{"id": "GroupCompanyId"}]
}

datadict1 = {
 'activeFrom': datetime.datetime(1986, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
 'activeTo': datetime.datetime(2050, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
 'comment': '',
 'displayed': True,
 'externalReference': '',
 'fillColor': {'a': 191, 'b': 0, 'g': 165, 'r': 255},
 'groups': [{'id': 'GroupCompanyId'}],
#  'id': 'b8',
 'mustIdentifyStops': True,
 'name': 'my Zone',
 'points': [{'x': -79.712318, 'y': 43.438266},
            {'x': -79.711181, 'y': 43.437461},
            {'x': -79.712677, 'y': 43.436168},
            {'x': -79.713966, 'y': 43.437107},
            {'x': -79.712318, 'y': 43.438266}],
 'zoneTypes': ['ZoneTypeOfficeId']
}

result = api.add('Zone',datadict1)
result
# api.add('Device', {
# 'serialNumber': 'GTA9000003EA',
# 'name': 'My Vehicle'
# })



