from datetime import datetime

time='05/24/22 23:24:17'
time=time.replace("\r","")

dt = datetime.strptime(time, '%m/%d/%y %H:%M:%S')

ts = datetime.timestamp(dt)

print("Date and time is:", dt)
print("Timestamp is:", int(ts))

