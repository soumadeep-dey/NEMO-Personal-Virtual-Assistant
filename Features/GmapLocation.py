import requests
from Features.Face.Mouth import speak
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web


def Getmylocation():
    ip_address = requests.get('https://api.ipify.org').text
    # ip_address = '110.224.1.87'
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_address + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f"You are currently located in {state},{country}")

def Getgmaplocation(place):
    place = place.replace("tell","")
    place = place.replace("destination","")
    place = place.replace("want to","")
    place = place.replace("go","")
    url_place = "https://www.google.com/maps/place/" + place
    geolocator = Nominatim(user_agent="my-Geocoder")
    location = geolocator.geocode(place , addressdetails = True)
    target_latlon = location.latitude , location.longitude
    location = location.raw['address']
    target = {'city': location.get('city',''),
                'state': location.get('state',''),
                'country': location.get('country','')}
    currentloc = geocoder.ip('me')
    currentlatlon = currentloc.latlng 
    distance = str(great_circle(currentlatlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    web.open(url=url_place)
    speak(f"{place} is {distance} kilometre away from your location.")

# Getmylocation()
# Getgmaplocation('howrah')