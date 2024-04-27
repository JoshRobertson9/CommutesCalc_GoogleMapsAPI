import requests
import requests_cache
import csv

#import json_tools


def commute_calc(file_name):
    # Caching turned on
    requests_cache.install_cache("locations_cache", expire_after=None)

    # API Prep
    with open("google-maps-api-key.txt","r") as api_file:
        api_key = api_file.read()

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"


    # Access - Read and Write
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        length = len(rows)

        # Re-used variables pulled
        try:
            base = rows[11][1]
            gas_price = float(rows[8][1])
            fuel_efficiency = float(rows[9][1])

        except IndexError:
            print("Index Error. Fix File or Code.")

        # Summation Variables
        # Total Weekly Drive Time (hours)
        twdt = 0
        
        # Total Weekly Commute Distance (miles)
        twcd = 0
        
        # Total Weekly Cost ($)
        twc = 0


        # For Loop
        for i in range(15,length):

            try:
                destination = rows[i][0]
                frequency = float(rows[i][1])

            except IndexError:
                print("Index Error. Fix File or Code.")

            r = requests.get(url + "origins=" + base + "&destinations=" + destination + "&key=" + api_key) 
            
            #json_tools.update_cache("locations_cache.json", r.json())

            # API Results
            seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
            minutes = round(seconds / 60, 2)
            hours = round(seconds / 3600, 2)
            distance = round(r.json()["rows"][0]["elements"][0]["distance"]["value"] / 1609, 2)

            # Print Results
            print(f"Traveling from {base} to {destination}:")

            if hours >= 1:
                print(f"The total travel time in hours is {hours} hours.")
            else:
                print(f"The total travel time in minutes is {minutes} minutes.")

            print(f"The total travel distance is {distance} miles.")

            # Additional Calculations

            # Weekly Round Trip Commute Time (hrs)
            wrtcth = round(frequency * (2* hours), 2)

            # Weekly Round Trip Commute Distance (miles)
            wrtcdm = round(frequency * (2* distance), 2)

            # Weekly Round Trip Fuel Cost (miles)
            wrtcc = round(wrtcdm * (gas_price / fuel_efficiency), 2)

            # Printing Additional Results

            print(f"The weekly round trip commute time is {wrtcth} hrs.")
            print(f"The weekly round trip commute distance is {wrtcdm} miles.")
            print(f"The weekly round trip fuel cost is ${wrtcc}.")
            print()

            # Updating the results for that entry
            rows[i][2] = hours
            rows[i][3] = minutes
            rows[i][4] = wrtcth
            rows[i][5] = distance
            rows[i][6] = wrtcdm
            rows[i][7] = wrtcc

            # Updating the summations
            twdt += wrtcth
            twcd += wrtcdm
            twc += wrtcc

        # Cleaning up the data
        twdt = round(twdt, 2)
        twcd = round(twcd, 2)
        twc = round(twc, 2)

        # Updating all the summation variables
        # Weekly Totals
        rows[4][1] = twdt
        rows[5][1] = twcd
        rows[6][1] = twc

        # Yearly Totals
        rows[0][1] = tydt = round(twdt * 52, 2)
        rows[1][1] = tycd = round(twcd * 52, 2)
        rows[2][1] = tyc  = round(twc * 52, 2)


    # Printing the Overall Values
    print("Weekly Commute Totals")
    print(f"The Total Weekly Drive time of this commute schedule is {twdt} hours.")
    print(f"The Total Weekly Commute distance of this commute schedule is {twcd} miles.")
    print(f"The Total Weekly Fuel Cost of this commute schedule is ${twc} cost.")
    print()

    print("Yearly Commute Totals")
    print(f"The Total Yearly Drive time of this commute schedule is {tydt} hours.")
    print(f"The Total Yearly Commute distance of this commute schedule is {tycd} miles.")
    print(f"The Total Yearly Fuel Cost of this commute schedule is ${tyc} cost.")
    print()

    # Writing all the results back to the file

    with open(file_name, mode="w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        
        print(f"The file {file_name} has been updated.")

    return base, twdt, twcd, twc
