import requests
import csv


# User Inputs

#base = "Detroit, MI"
#destination = "Atlanta, GA"
filename = "locations.csv"

with open(filename, "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

    print()
    print(rows)
    print(len(rows))
    print()

    try:
        base = rows[11][1]
        gas_price = float(rows[8][1])
        fuel_efficiency = float(rows[9][1])

        destination = rows[15][0]
        frequency = float(rows[15][1])

    except IndexError:
        print("Index Error. Fix File or Code.")

#print(base)
#print(destination)


# API Key

api_file = open("google-maps-api-key.txt","r")
api_key = api_file.read()
api_file.close()


# API Call

# https://maps.googleapis.com/maps/api/distancematrix/outputFormat?parameters

url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

r = requests.get(url + "origins=" + base + "&destinations=" + destination + "&key=" + api_key)

# API Results

#time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
minutes = round(seconds / 60, 2)
hours = round(seconds / 3600, 2)

# Distance in miles as a str
#distance_str = r.json()["rows"][0]["elements"][0]["distance"]["text"]
# Distance in miles as a float
distance = round(r.json()["rows"][0]["elements"][0]["distance"]["value"] / 1609, 2)

# Display Results

print(f"Traveling from {base} to {destination}:")
#print(f"The total travel time is {time}.")
#print(f"The total travel time in seconds is {seconds} seconds.")

if hours >= 1:
    print(f"The total travel time in hours is {hours} hours.")
else:
    print(f"The total travel time in minutes is {minutes} minutes.")



#print(f"The total travel distance is {distance_str}.")
print(f"The total travel distance is {distance} miles.")


# Additional Calculations

# Weekly Round Trip Commute Time (hrs)
wrtcth = frequency * (2* hours)

# Weekly Round Trip Commute Distance (miles)
wrtcdm = frequency * (2* distance)

# Weekly Round Trip Fuel Cost (miles)
wrtcc = round(wrtcdm * (gas_price / fuel_efficiency),2)


# Additional Results

print(f"The weekly round trip commute time is {wrtcth} hrs.")
print(f"The weekly round trip commute distance is {wrtcdm} miles.")
print(f"The weekly round trip fuel cost is ${wrtcc}.")


# Writing all of the results back to the file

rows[15][2] = hours
rows[15][3] = minutes
rows[15][4] = wrtcth
rows[15][5] = distance
rows[15][6] = wrtcdm
rows[15][7] = wrtcc


with open(filename, mode="w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("The CSV has been updated.")

