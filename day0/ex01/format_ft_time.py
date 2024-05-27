import datetime
import time

current_datetime = time.time()
timestamp = current_datetime
date = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)

formatted_date = "{:,.4f}".format(timestamp)

print("Seconds since January 1, 1970:", formatted_date, "or {:.2e}".format(current_datetime), "in scientific notation")
print(time.strftime("%b %d %Y"))