from common import *

voivodeship_unemployment = {
	'Małopolskie': 4.6,
	'Śląskie': 4.4,
	'Wielkopolskie': 3.2,
	'Zachodniopomorskie': 7.1,
	'Lubuskie': 5.0,
	'Dolnośląskie': 4.9,
	'Opolskie': 6.0,
	'Kujawsko-pomorskie': 7.7,
	'Warmińsko-mazurskie': 8.6,
	'Pomorskie': 5.3,
	'Łódzkie': 5.8,
	'Świętokrzyskie': 7.3,
	'Lubelskie': 7.1,
	'Podkarpackie': 8.1,
	'Podlaskie': 7.0,
	'Mazowiecki': 8.6
}

voivodeship_names = list(voivodeship_unemployment.keys())

def retrieve_lat_long(voivodeship_name):
	geolocator = Nominatim(user_agent=app_name)
	location = geolocator.geocode(f"{voivodeship_name}, Poland")
	latitude = location.latitude
	longitude = location.longitude
	return latitude, longitude

voivodeship_lat_long = {}
for voivodeship_name in voivodeship_names:
	voivodeship_lat_long[voivodeship_name] = retrieve_lat_long(voivodeship_name)

# Cache the files
open("data/voivodeship_lat_long.txt", "w").write(str(voivodeship_lat_long))
open("data/voivodeship_unemployment.txt", "w").write(str(voivodeship_unemployment))
open("data/voivodeship_names.txt", "w").write(str(voivodeship_names))
