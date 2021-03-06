import requests

place_list = [('Al Ain', 24.1302, 55.8023),('Paris', 48.8566, 2.3522),('Amsterdam', 52.3667, 4.8945),('Fort Valley', 32.5538, 83.8874),('New York', 40.7128, 74.0060),('Brussels', 50.8503, 4.3517),('Dubai', 25.2048, 55.2708), ('Atlanta', 33.7490, 84.3880),('Peachtree City', 33.3969, 84.5963),('Miami', 25.7617, 80.1918)]


def location_list(locations):
    weather_info = {}
    for location in locations:
      url = "https://api.climacell.co/v3/weather/realtime"
      payload = {
      "apikey":"biXVooJDskya6UZPsOlrS1l5TNLwNJUP",
      "lat":location[1],
      "lon":location[2],
      "fields":["temp", "feels_like", "moon_phase", "sunrise", "sunset"], "unit_system":"us",
      }
      response = requests.get(url, params=payload).json()
      weather_info[location[0]] = (response["temp"]["value"],response["feels_like"]["value"])
    # print(weather_info)
    for city, temp in weather_info.items():
     # print(temp) this will show bot hof the values that represent temp (TUPLE)
      print(f"The temp is {temp[0]} degrees in {city}, and it feels like {temp[1]}.")
      #this is a format statement that will print what we want it to say, and both of the temperatures, actual and feels like 
    return weather_info

location_list(place_list)

# If you want to use classes
# class Location:
#   def __init__(self, name, lat, lon):
#     self.lat = lat
#     self.lon = lon
#     self.name = name
  
#   def __str__(self):
#     # return " of ".join((self.lat, self.lon, self.name))
#     return(f'{self.name} latitude: {self.lat} longitude:{self.lon}')

# def create_placelist(list):
#   places = []
#   for city in list:
#     place = Location(city, city, city)
#     places.append(place)
#   return places
#   # for place in places:
#   #   print(place)

# places = create_placelist(place_list)

# print(places)

# # for place in places:
# #   print(place.name)

# # print(places[1].long)
# #when you actually get a class and you call it on that class you choose real values 
# # print(places)

# # def __init__(self):

# # def get__weather_data(location_list):

# #   pass

# def get_weather_data(lat, lon):

#   get_weather_data(24.1302, 55.8023)