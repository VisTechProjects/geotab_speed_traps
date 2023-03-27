import requests
import pprint
response = requests.get('https://services3.arcgis.com/b9WvedVPoizGfvfD/ArcGIS/rest/services/COT_SPEED_CAMERAS/FeatureServer/0/query?where=1%3D1%20&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&token=&f=json')

if response.status_code == 200:
    print("Succesful connection with API.")
    print('-------------------------------')
    data = response.json()
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

elif response.status_code == 404:
    print("Unable to reach URL.")
else:
    print("Unable to connect API or retrieve data.")