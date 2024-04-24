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
        choice = input("\nType in your choice (1, 2, or 3). ")
        
except ValueError:
        print("You provided an incorrect input, so it will default to 1.")
        choice = "1"

match choice:
        case "1":
            commutes.commute_calc(file_name1)

        case "2":
            where_to_live.where_to_live_calc(file_name1,file_name2)

        case "3":
            pass
            #central_location.central_location()
