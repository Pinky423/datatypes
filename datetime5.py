from datetime import datetime

date_str = "2024-01-01"

dt = datetime.strptime(date_str, "%Y-%m-%d")

print("Datetime object:", dt)

print(dt.strftime("%Y-%m-%d %H:%M:%S"))