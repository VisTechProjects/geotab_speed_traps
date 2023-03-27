import os
import mygeotab
import datetime
import pprint
import requests
with open(os.path.abspath( os.path.dirname( __file__ )) + "\geotab_login.txt", 'r') as file:
    loginpw = file.read().rstrip()

api = mygeotab.API(username='vismantaskuznecovas@gmail.com',
                   password=loginpw, database='vis')
api.authenticate()

# result = api.get('Device', resultsLimit=2)
# result

speed_camera_zones_API_response = requests.get('https://services3.arcgis.com/b9WvedVPoizGfvfD/ArcGIS/rest/services/COT_SPEED_CAMERAS/FeatureServer/0/query?where=1%3D1%20&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&token=&f=json')

result = api.get('Zone')
pprint.pprint(result[6])

def add_zone():

    datadict1 = {
    'activeFrom': datetime.datetime(1986, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
    'activeTo': datetime.datetime(2050, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
    'comment': '',
    'displayed': True,
    'externalReference': '',
    'fillColor': {'a': 191, 'b': 0, 'g': 165, 'r': 255},
    'groups': [{'id': 'GroupCompanyId'}],
    'mustIdentifyStops': True,
    'name': 'my Zone',
    'points': [{'x': -79.712318, 'y': 43.438266},
                {'x': -79.711181, 'y': 43.437461}, # find formula for square 
                {'x': -79.712677, 'y': 43.436168},
                {'x': -79.713966, 'y': 43.437107}],
                
    'zoneTypes': ['ZoneTypeOfficeId']
    }

    result = api.add('Zone',datadict1)
    result

def get_speed_camera_zones():
    if speed_camera_zones_API_response.status_code == 200:
        print("Succesful connection with API.")
        print('-------------------------------')
        data = speed_camera_zones_API_response.json()
        data = data['features']
        # pprint.pprint(data)

        print("got " + str(len(data)) + " locations")

        for data_point in data:
            if(data_point['attributes']['Status'] == 'Active'):
                # pprint.pprint(data_point['attributes'])
                print("\nlat:" + str(data_point['attributes']['lat']))
                print("long:" + str(data_point['attributes']['long']))
                print("location:" + str(data_point['attributes']['location']))
                print("ward:" + str(data_point['attributes']['Ward']))

    elif speed_camera_zones_API_response.status_code == 404:
        print("Unable to reach URL.")
    else:
        print("Unable to connect API or retrieve data.")


if __name__ == "__main__":
    add_zone() 
    # get_speed_camera_zones()