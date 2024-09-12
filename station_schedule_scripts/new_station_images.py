import requests
import json

import os


file_path = "/home/adcuratio/Desktop/Study/station_schedule_scripts/stations_dict.json"

try:
    # Open the file and load the JSON data
    with open(file_path, "r") as json_file:
        file_data = json.load(json_file)

        # Extracting id_2.0 into station_ids list
    station_ids = [station["id_2.0"] for station in file_data.values()]

    print("Station IDs:")
    print(station_ids)

    print("\nRead JSON data from 'stations_dict.json':")

except FileNotFoundError:
    print(f"The file was not found at {file_path}. Please check the file path.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from {file_path}. Ensure the file contains valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


unique_dimensions = {} 


for id in station_ids:
    # Define the URL and parameters
    url = 'https://lla-metadata-prod-elb.digitalsmiths.net/sd/8454d541094352a9/taps/v3/idLookup'
    params = {
        'rovi2': f'st-{id}',
        'includeAllFields': 'true'
    }

    # Send the GET request
    response = requests.get(url, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        # Extract the images from the response
        hits = data.get('hits', [])
         # Use a set to keep dimensions unique
        
        for hit in hits:
            images = hit.get('images', [])
            for image in images:
                width = image.get('width')
                height = image.get('height')
                if width is not None and height is not None and url[-10:-4] == "_white":
                    # Create the w_h key and update the frequency
                    print("found")
                    w_h_key = f'{width}_{height}'
                    unique_dimensions[w_h_key] = unique_dimensions.get(w_h_key, 0) + 1
        

        # Write to a JSON file
        with open('unique_dimensions.json', 'w') as json_file:
            json.dump(unique_dimensions, json_file, indent=4)

        print("Unique dimensions saved to 'unique_dimensions.json'.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

