import commutes
import where_to_live

# You can change this to the name of whatever local file you want as long as internally the file has the same layout as this template file.
file_name1 = "locations1.csv"
file_name2 = "locations2.csv"

try:
        print("Hello, would you like to know the commute schedule based on one starting location or compare the commutes of two locations?")
        choice = input("Type 1 or 2 depending on you choice. ")
except ValueError:
        print("You provided an incorrect input, so it will default to 1.")
        choice = "1"
     
if choice == "1":

    commutes.commute_calc(file_name1)

elif choice == "2":

    where_to_live.where_to_live_calc(file_name1,file_name2)
