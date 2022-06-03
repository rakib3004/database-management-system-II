from datetime import datetime
import random

from scipy import rand

time='05/24/22 23:24:17'
time=time.replace("\r","")

dt = datetime.strptime(time, '%m/%d/%y %H:%M:%S')

ts = datetime.timestamp(dt)

print("Date and time is:", dt)
print("Timestamp is:", int(ts))

for i in range(100):
    print(random.randint(0,60))
