import requests_cache

# My created Modules
import commutes
import where_to_live
import central_location

# You can change this to the name of whatever local file you want as long as internally the file has the same layout as this template file.
file_name1 = "locations1.csv"
file_name2 = "locations2.csv"

try:
        #print("Hello, would you like to know the commute schedule based on one starting location or compare the commutes of two locations?")
        print("\nThis is the commute calculation tool that allows for various calculations using Google Map's API.\n")
        print("1. Commute from one location to several locations.")
        print("2. Coparing the overall commutes of two starting locations.")
        print("3. Finding the central meeting place for a list of locations.")
        print("4. Clear cache.")
        choice = input("\nType in your choice (1 - 4). ")
        
except ValueError:
        print("You provided an incorrect input, so it will default to 1.")
        choice = "1"

match choice:
        # Commute Calculation for 1 location to many
        case "1":
            commutes.commute_calc(file_name1)

        # Commute Calulation comparing 2 starting locations to many
        case "2":
            where_to_live.where_to_live_calc(file_name1,file_name2)

        # Finding the central location
        case "3":
            central_location.central_location()

        case "4":
            #requests_cache.get_cache('locations_cache').clear()
            #requests_cache.clear('locations_cache')
            requests_cache.install_cache("locations_cache", expire_after=None)
            requests_cache.clear()

            requests_cache.install_cache("central_loc_cache", expire_after=None)
            requests_cache.clear()

            print("Cache cleared")
            # other cache