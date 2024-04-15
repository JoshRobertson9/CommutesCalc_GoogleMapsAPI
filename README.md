# CommutesCalc_GoogleMapsAPI
This tool takes one starting address and any number of other destinations and calculates the commute time, distance, and fuel cost using the Google Maps API and writes the results to a csv. 

It can take this data and project it out over a week based on some frequency and even a year.

If you don't want to think of this in terms of a frequency you can just ignore the additional outputs for that, but will still need a frequency of 1.

To Run:

You will need to pre-enter these addresses into the "locations.csv" file.

Next you will also need to clear out any existing output results in the "locations.csv" file.

Last, you will need your own API key for Google Maps and save it in the "google-maps-api-key.txt" file.

After those three requirements are all set you can run the "commutes.py" file from there.

If you wanted, you can even make a copy of and rename the CSV file afterwards to run/save multiple scenarios.

For reference, there are only 2 API requests per base location to destination calculation.

I have built this on my own, but definitely took some inspiration from this video to know which commmands were best to use and how to set it up initially.

https://www.youtube.com/watch?v=yOXQAmYl0Aw