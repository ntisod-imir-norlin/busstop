import requests

from datetime import datetime

from settings import key_plats,key_departures

def sites(searchstring):
    url = "http://api.sl.se/api2/typeahead.json?key={key}&searchstring={searchstring}"

    # download the page from trafiklab
    resp = requests.get(url.format(key=key_plats,searchstring = searchstring))



    return  resp.json()['ResponseData']

def departures(siteid):
    url ="http://api.sl.se/api2/realtimedepartures.json?key={key}&siteid={siteid}&timewindow=60"

    print url


    # download the page from trafiklab
    resp = requests.get(url.format(key=key_departures,siteid = siteid))


    trains= resp.json()["ResponseData"]["Trains"][:10]

    for train in  trains:
        dt = datetime.strptime(train['ExpectedDateTime'],'%Y-%m-%dT%H:%M:%S')

        train['TExpectedDateTime']= "{hour}:{minute:02d}".format(hour=dt.hour,minute=dt.minute)

        train['TTimeLeft']="9 min"


    return trains

