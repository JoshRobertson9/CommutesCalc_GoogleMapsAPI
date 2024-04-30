# CommutesCalc_GoogleMapsAPI

## Overview

This tool can perform a number of different calculations relating to the driving commutes between a number of different places using the Google Maps API.

## Tools

- One feature calculates commute time, distance, and fuel cost  based on a starting address and one or more destinations. Results are written to a CSV file. It can project data over a week and a year based on a weekly frequency.
- A second feature is the same as the first, but compares two commute files between their overall values. You can have different starting and ending locations for either file.
- The third feature finds the central location based on a provided list of locations.

## Features

- Calculate commute time, distance, and fuel cost.
- Project commute data over a week and a year.
- Compare commutes between two locations.
- Find the central location of a list of locations.
- Cached API calls for reusability.

## Usage

1. Enter addresses into "locations1.csv" and optionally "locations2.csv" for comparison.
2. Clear existing output results in "locations1.csv", "locations2.csv", and "central_location.csv".
3. Save your Google Maps API key in "google-maps-api-key.txt".
4. Run "main.py" to execute the tool.
5. Optionally, make copies of CSV files for multiple scenarios and change their name as needed.

## Additional Information

- Each base location to destination calculation requires only 2 API requests.
- Inspiration taken from [this video](https://www.youtube.com/watch?v=yOXQAmYl0Aw).
- Assistance provided by ChatGPT for understanding API calls.
- For a detailed example output, refer to "example_result.txt".
- In this tool all values for a round trip are just 2x the values for a one way trip. In reality it could be a slightly different commute each way.
