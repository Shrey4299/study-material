from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current local date and time:", now)

# Current UTC date and time
utc_now = datetime.utcnow()
print("Current UTC date and time:", utc_now)

# Formatting datetime
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted)

# Parsing datetime
parsed = datetime.strptime("2023-04-15 12:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed)

# Adding and subtracting timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
yesterday = now - one_day
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)
