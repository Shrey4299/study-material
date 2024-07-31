import json

# Load the JSON data from the file
with open("station_sample.json") as f:
    data = json.load(f)

# Initialize an empty dictionary to store the results
station_dict = {}

# Iterate through each item in the JSON data
for item in data:
    hsa_station_id = item.get("hsa_station_id")
    program_data = item.get("programdata", [])

    # Initialize counters
    program_with_image_count = 0
    program_with_image_w_h_count = 0

    # Count programs with images within programdata
    for program in program_data:
        has_image = ("programImages" in program and program["programImages"]) or (
            "seriesImages" in program and program["seriesImages"]
        )
        if has_image:
            program_with_image_count += 1

            # Check image width-to-height ratio
            if "programImages" in program and program["programImages"]:
                for img in program["programImages"]:
                    width = img.get("width", 0)
                    height = img.get("height", 0)
                    if height > 0 and width / height > 1.5:
                        program_with_image_w_h_count += 1
                        break

            if (
                "seriesImages" in program
                and program["seriesImages"]
                and program["programData"][0]["objectType"] in ["Episode","SportsEvent"]
            ):
                for img in program["seriesImages"]:
                    width = img.get("width", 0)
                    height = img.get("height", 0)
                    if height > 0 and width / height > 1.5:
                        program_with_image_w_h_count += 1
                        break

    # Check if the hsa_station_id already exists in the dictionary
    if hsa_station_id in station_dict:
        station_dict[hsa_station_id]["program_count"] += len(program_data)
        station_dict[hsa_station_id]["program_with_image"] += program_with_image_count
        station_dict[hsa_station_id][
            "program_with_image_w_h"
        ] += program_with_image_w_h_count
    else:
        station_dict[hsa_station_id] = {
            "program_count": len(program_data),
            "program_with_image": program_with_image_count,
            "program_with_image_w_h": program_with_image_w_h_count,
        }

# Save the resulting dictionary to a JSON file
with open("station_results.json", "w") as f:
    json.dump(station_dict, f, indent=4)

print("Results saved to station_results.json")
