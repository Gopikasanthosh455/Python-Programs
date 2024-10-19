#25. Calculate number of days between two given dates

from datetime import datetime

date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

difference = abs((date2 - date1).days)

print("Number of days between", date_str1, "and", date_str2, "is:", difference)
