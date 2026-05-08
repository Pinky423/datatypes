from datetime import datetime

date = input("Enter date (DD-MM-YYYY): ")

d = datetime.strptime(date, "%d-%m-%Y")

print("Day:", d.strftime("%A"))