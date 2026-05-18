from utilities import file_utils, date_utils
from datetime import date

file_utils.write_file()
file_utils.read_file()

d1 = date(2024, 1, 1)
d2 = date(2024, 1, 10)

print(date_utils.days_between(d1, d2))