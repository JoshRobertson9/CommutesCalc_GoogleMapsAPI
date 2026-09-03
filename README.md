# CommutesCalc_GoogleMapsAPI

## Overview

This tool can perform various calculations relating to the driving commutes between any number of locations using the Google Maps API.

## Tools

- One tool calculates commute time, distance, and fuel cost based on a starting address and one or more destinations. Results are written to a CSV file. It can project data over a week and a year based on a weekly frequency.
- A second tool is the same as the first, but compares two commute files between their overall values. You can have different starting and ending locations for either file.
- The third tool finds the central location based on a provided list of locations.

## Features

- Calculate commute time, distance, and fuel cost.
- Project commute data over a week and a year.
- Compare commutes between two locations.
- Find the central location of a list of locations.
- Cached API calls for reusability.

## Requirements

- Python 3.10 or newer (the menu uses `match` statements).
- Install dependencies: `pip install -r requirements.txt`
- A Google Maps API key with the **Distance Matrix API** (Tools 1 and 2) and the
  **Geocoding API** (Tool 3) enabled. Save it in `google-maps-api-key.txt` in the
  project root. This file is gitignored.

## Usage - Tools 1 and 2

1. Clear existing output results and enter new addresses in "locations1.csv" and optionally "locations2.csv" if you want to do a comparison.
2. Save your Google Maps API key in "google-maps-api-key.txt".
3. Run "main.py" to execute the tool.
4. Select option 1 or 2.
5. You can also clear the cache with option 4 if you want more recent information.
6. Optionally, make copies of CSV files for multiple scenarios and change their name as needed.

## Usage - Tool 3

1. Clear existing output results and enter new addresses in "central_location.csv".
2. Save your Google Maps API key in "google-maps-api-key.txt".
3. Run "main.py" to execute the tool.
4. Select option 3.
5. You can also clear the cache with option 4 if you want more recent information.
6. Optionally, make copies of CSV files for multiple scenarios and change their name as needed.

## Additional Information

- Each base location to destination calculation requires only 2 API requests.
- Inspiration taken from [this video](https://www.youtube.com/watch?v=yOXQAmYl0Aw).
- For a detailed example output, refer to "example_result.txt".
- In this tool all values for a round trip are just 2x the values for a one way trip. In reality it could be a slightly different commute each way.

## Security Scanning
[![Scanned by Frogbot](https://raw.github.com/jfrog/frogbot/master/images/frogbot-badge.svg)](https://docs.jfrog-applications.jfrog.io/jfrog-applications/frogbot)
