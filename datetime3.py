from datetime import datetime

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%m/%d/%Y"))

print(now.strftime("%H:%M:%S"))  
print(now.strftime("%I:%M:%S %p"))  