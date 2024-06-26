# Existing Module
import requests
import requests_cache
import csv

# Get the longitude and latitude from a give location
def get_longlat_from_loc(location):

    # Caching turned on to store and reuse api calls
    requests_cache.install_cache("central_loc_cache", expire_after=None)

    # API Prep
    with open("google-maps-api-key.txt","r") as api_file:
        api_key = api_file.read()

        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"
        response = requests.get(url)
        data = response.json()

    if data['status'] == 'OK':
        longitude = data['results'][0]['geometry']['location']['lng']
        latitude = data['results'][0]['geometry']['location']['lat']
        return longitude, latitude 

    else:
        print("Failed to get coordinates.")
        return None, None

# Get a location based on a given longitue and latitude
def get_loc_from_longlat(longitude,latitude):

    # Caching turned on to store and reuse api calls
    requests_cache.install_cache("central_loc_cache", expire_after=None)

    # API Prep
    with open("google-maps-api-key.txt","r") as api_file:
        api_key = api_file.read()

    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        address = data['results'][0]['formatted_address']
        return address
    else:
        print("Failed to get address.")
        return None

# Determine the central location of a list of locations based on longitude and latitude
def central_location():
    
    # Used for other functions.
    # Caching turned on to store and reuse api calls
    #requests_cache.install_cache("central_loc_cache", expire_after=None)

    # API Access - other functions make the apicall
    #with open("google-maps-api-key.txt","r") as api_file:
    #    api_key = api_file.read()

    with open("central_location.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        length = len(rows)

        longs = []
        lats = []

        print("Locations:")

        # Looping through each location to consider
        for i in range(3,length):

            try:
                location = rows[i][0]
                print(location)

            except IndexError:
                print("Index Error. Fix File or Code.") 

            # Using function I wrote to get longitude and latitude
            long, lat = get_longlat_from_loc(location)

            rows[i][1] = long
            rows[i][2] = lat

            longs.append(long)
            lats.append(lat)

    # Printing Results
    central_long = sum(longs)/len(longs)
    central_lat = sum(lats)/len(lats)
    print(f"The central location is {central_long}, {central_lat}.")

    central_loc = get_loc_from_longlat(central_long,central_lat)
    print(f"The central location is at {central_loc}.")

    # Updating the central location values
    rows[1][0] = central_loc
    rows[1][1] = central_long
    rows[1][2] = central_lat

    # Writing the central location to the csv file
    with open("central_location.csv", mode="w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        print(f"The central_location.csv file has been updated.")

if __name__ == "__main__":
    central_location()
    # Simple Example
    longitude, latitude = get_longlat_from_loc("Detroit, MI")
    print(longitude)
    print(latitude)