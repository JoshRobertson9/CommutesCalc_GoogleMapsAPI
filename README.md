# CommutesCalc_GoogleMapsAPI

Notes:

This tool takes one starting address and any number of other destinations and calculates the commute time, distance, and fuel cost using the Google Maps API and writes the results to a csv. 

It can take this data and project it out over a week and a year based on a weekly frequency.

If you don't want to think of this in terms of a frequency you can just ignore the additional outputs for that, but will still need a frequency value of 1.

Now you can also compare the commutes of two locations. Imagine if you were trying to buy a house. Now you could see which is overall closer to the places you frequently visit. The locations files are separate in case any of the destinations change based on the different starting locations.

If you don't have a Google API key, but want to see how this works, you can read an example terminal output corresponding to the current location csv files in the file "example_result.txt".

To Run:

You will need to pre-enter these addresses into the "locations1.csv" file.

Next you will also need to clear out any existing output results in the "locations1.csv" file for now.

If you want to compare two locations you will need to do the same for "locations2.csv" with the information for the second location.

Last, you will need your own API key for Google Maps and save it in the "google-maps-api-key.txt" file.

After those three requirements are all set you can run the "commutes.py" file from there.

If you wanted, you can even make a copy of and rename the CSV file afterwards to run/save multiple scenarios.

For reference, there are only 2 API requests per base location to destination calculation.

I have built this on my own, but took inspiration from this video to know which commmands were best to use and how to set it up initially.

https://www.youtube.com/watch?v=yOXQAmYl0Aw