# Existing Modules
import commutes

# Comparing two commute sets
def where_to_live_calc(file_name1, file_name2):

    # Location 1 Commutes
    start_loc1, twdt1, twcd1, twc1 = commutes.commute_calc(file_name1)
    print()

    # Location 2 Commutes
    start_loc2, twdt2, twcd2, twc2 = commutes.commute_calc(file_name2)
    print()

    # Comparing the two location's commutes
    print(f"Here is the comparison of {start_loc1} vs {start_loc2}.")
    compare(start_loc1, twdt1, start_loc2, twdt2, "weekly commute time","hours")
    compare(start_loc1, twcd1, start_loc2, twcd2, "weekly commute distance","miles")
    compare(start_loc1, twc1, start_loc2, twc2, "weekly commute cost","$")

# Compares various values of a commute
def compare(start_loc1, value1, start_loc2, value2, category_string, unit_string):
    # Ex category_string = "weekly commute cost"
    # Ex unit_string = "hours"

    if value1 == value2:
        print(f"Both locations have the same total {category_string} of {round(value1,2)}. ",category_string)

    elif value1 < value2:
        if unit_string == "$":
            print(f"{start_loc1} has a lower total {category_string}, beating the other option by {unit_string}{round(value2-value1, 2)}.")
        else : 
            print(f"{start_loc1} has a lower total {category_string}, beating the other option by {round(value2-value1, 2)} {unit_string}.")

    elif value1 > value2:
        if unit_string == "$":
            print(f"{start_loc2} has a lower total {category_string}, beating the other option by {unit_string}{round(value1-value2, 2)}.")
        else : 
            print(f"{start_loc2} has a lower total {category_string}, beating the other option by {round(value1-value2, 2)} {unit_string}.")