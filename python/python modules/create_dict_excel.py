import pandas as pd

# Load the Excel file
file_path = "/home/adcuratio/Downloads/llapr_stations UPDATED.xlsx"  # Update this path to your actual file path
excel_data = pd.read_excel(file_path)

# Create the dictionary
stations_dict = {}

for _, row in excel_data.iterrows():
    partner_station = f"epgProvider:st.{row['partner_station_id']}"
    station_details = {
        "id_2.0": row["2.0_id"],
        "call_sign": row["call_sign"],
        "station_name": row["station_name"],
        "packaged_service _description": (
            row["packaged_service _description"]
            if pd.notna(row["packaged_service _description"])
            else None
        ),
    }
    stations_dict[partner_station] = station_details

# Optionally, display or save the dictionary
print(stations_dict)

# Save the dictionary to a file if needed
import json

with open("stations_dict.json", "w") as json_file:
    json.dump(stations_dict, json_file, indent=4)
