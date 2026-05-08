from datetime import datetime, timedelta

d1 = datetime(2024, 1, 1)
d2 = datetime(2024, 1, 10)

diff = d2 - d1

print("Days between:", diff.days)

today = datetime.now()
new_date = today + timedelta(days=7)

print("After 7 days:", new_date)