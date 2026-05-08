from datetime import datetime
import pytz

utc = datetime.now(pytz.utc)

local = datetime.now()

print("UTC Time:", utc)
print("Local Time:", local)