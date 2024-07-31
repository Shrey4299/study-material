import json

# Load the JSON data from the file
with open("lla.station_schedules.json") as f:
    data = json.load(f)

# Initialize a list to store images with a width-to-height ratio > 1.5
filtered_images = []

# Iterate through each item in the JSON data
for item in data:
    program_data = item.get("programdata", [])

    # Check images within programdata
    for program in program_data:
        if "programImages" in program:
            for img in program["programImages"]:
                width = img.get("width", 0)
                height = img.get("height", 0)
                if height > 0 and width / height > 1.5:
                    filtered_images.append(img)
        if "seriesImages" in program:
            for img in program["seriesImages"]:
                width = img.get("width", 0)
                height = img.get("height", 0)
                if height > 0 and width / height > 1.5:
                    filtered_images.append(img)

    # Check images outside of programdata
    program_images = item.get("programImages", [])
    series_images = item.get("seriesImages", [])

    for img in program_images + series_images:
        width = img.get("width", 0)
        height = img.get("height", 0)
        if height > 0 and width / height > 1.5:
            filtered_images.append(img)

# Save the filtered images to a new JSON file
with open("filtered_images.json", "w") as f:
    json.dump(filtered_images, f, indent=4)

print("Filtered images have been saved to 'filtered_images.json'.")
