from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_geocoding_app")
zip_data = input("enter the zip code:")
zipcode = zip_data

location = geolocator.geocode(zipcode)
print("Zipcode: " + zipcode)
print("Details of the Zipcode: ")
print(location)
