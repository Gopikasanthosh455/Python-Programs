from datetime import date, timedelta

today = date.today()
print("Today:", today)

for i in range(1, 6):
    next_day = today + timedelta(days=i)
    print("Day", i, ":", next_day)
