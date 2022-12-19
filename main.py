from common import *
center_of_poland = (52.237049, 21.017532)

# 1st task
voivodeship_lat_long = eval(open("data/voivodeship_lat_long.txt").read())
open("results/1_task.txt", "w").write(str(voivodeship_lat_long))

voivodeship_unemployment = eval(open("data/voivodeship_unemployment.txt").read())
voivodeship_names = eval(open("data/voivodeship_names.txt").read())

# 2nd task
# Create a map centered on the center of Poland
m = folium.Map(location=list(center_of_poland), zoom_start=6)
geolocator = Nominatim(user_agent=app_name)
# add a circle for each voivodoship
for voivodoship, unemployment in voivodeship_unemployment.items():
	print(f"Adding {voivodoship} to the map")
	location = geolocator.geocode(voivodoship + ", Poland")
	# 3rd task - Popup content
	popup_content = f"{voivodoship} has {unemployment}% unemployment"
	folium.Circle(
		location=[location.latitude, location.longitude],
		radius=unemployment*1000, # scale the radius by a factor of 1000 for better visualization
		popup=popup_content,
		color="red",
		fill=True,
		fill_color="red"
	).add_to(m)
# save the map
m.save("results/2_task.html")

# Display the map
m