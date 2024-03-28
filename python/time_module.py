import pytz
from datetime import datetime

# Example UTC datetime string
utc_datetime_str = "2023-07-15T09:30:00.123Z"
time_zone_str = "Asia/Kolkata"  # Changing to Indian Standard Time (IST)

# Set the time zone based on the input string
target_time_zone = pytz.timezone(time_zone_str)

# Convert the UTC datetime to the specified local time zone
utc_datetime = datetime.strptime(utc_datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
local_datetime = utc_datetime.replace(tzinfo=pytz.utc).astimezone(target_time_zone)

# Get the current time in the specified timezone
current_time = datetime.now(target_time_zone)

# Get the UTC offset for the current time
offset_hours = current_time.utcoffset().total_seconds() / 3600

# Print the results
print("UTC Datetime:", utc_datetime)
print("Local Datetime:", local_datetime)
print("Current Time in", time_zone_str, ":", current_time)
print("UTC Offset:", offset_hours, "hours")
