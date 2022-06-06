from datetime import datetime
from datetime import date



now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


today = date.today()
print("Today's date:", today)




