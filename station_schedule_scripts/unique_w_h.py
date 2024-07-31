import json

# Load the JSON file
with open(
    "/home/adcuratio/Desktop/Study/station_schedule_scripts/filtered_images.json", "r"
) as file:
    data = json.load(file)

# Initialize a set to store unique width and height combinations
unique_dimensions = set()

# List to store the new JSON objects
new_data = []

# Iterate over the images and collect unique width and height combinations
for image in data:
    width = image["width"]
    height = image["height"]
    dimensions = (width, height)

    if dimensions not in unique_dimensions:
        unique_dimensions.add(dimensions)
        new_object = {
            "id": f"{width}_{height}",
            "width": width,
            "height": height,
            "contentType": image["contentType"],
        }
        new_data.append(new_object)

# Write the new JSON objects to a new file
with open("unique_images.json", "w") as outfile:
    json.dump(new_data, outfile, indent=4)

print("New JSON file with unique dimensions created successfully.")
