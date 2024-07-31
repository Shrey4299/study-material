import pytz
from datetime import datetime, timedelta

# # Get today's date at 12 AM UTC
# utc_datetime = datetime.utcnow()
utc_datetime_str = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
time_zone_str = "Asia/Kolkata"  # Changing to Indian Standard Time (IST)


# Get the current time in the specified timezone
# tz = pytz.timezone(time_zone_str)

# Format the datetime
registration_date_time = datetime.now(pytz.timezone(time_zone_str)).strftime(
    "%Y-%m-%dT%H:%M:%S.%f%z"
)

print(f"Registration DateTime: {registration_date_time}")


# # Set the time zone based on the input string
# target_time_zone = pytz.timezone(time_zone_str)

# # Convert the UTC datetime to the specified local time zone
# utc_datetime = datetime.strptime(utc_datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
# local_datetime = utc_datetime.replace(tzinfo=pytz.utc).astimezone(target_time_zone)

# # Get the current time in the specified timezone
# current_time = datetime.now(target_time_zone)

# # Add 7 hours to the current time and save as time2
# time2 = current_time + timedelta(hours=7)

# # Get the UTC offset for the current time
# offset_hours = current_time.utcoffset().total_seconds() / 3600

# Print the results
# print("UTC Datetime:", utc_datetime)
# print("Local Datetime:", local_datetime)
# print("Current Time in", time_zone_str, ":", current_time)
# print("Time2 (Current Time + 7 hours):", time2)
# print("UTC Offset:", offset_hours, "hours")

print(utc_datetime_str)
