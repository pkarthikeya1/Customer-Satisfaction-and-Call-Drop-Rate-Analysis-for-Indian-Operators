import pandas as pd
import geopy.geocoders as geocoders


# Assuming your dataframe is called 'df' and has columns 'latitude' and 'longitude'

# Choose a geocoder service (e.g., Nominatim is free and open-source)
geolocator = geocoders.Nominatim(user_agent="individual_use", timeout=10)  # Replace with your app name

# Define a function to perform geocoding and extract state name
def get_state_name(row):
    latitude = row['latitude']
    longitude = row['longitude']
    location = geolocator.reverse((latitude, longitude), timeout=10)
    if location:  # Check if location data is available
        state_name = location.address.split(",")[-3]
        return state_name
    else:
        return None  # Handle cases where location data is missing

