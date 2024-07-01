#1 Subtract five days from the current date:
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print(current_date)
print(five_days_ago)

#2 Print yesterday, today, and tomorrow:
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)


#3 Drop microseconds from datetime:
from datetime import datetime

current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print(current_datetime)
print(current_datetime_without_microseconds)



#4 Calculate the difference between two dates in seconds:
from datetime import datetime

date_str1 = '2023-06-15 12:00:00'
date_str2 = '2023-06-20 08:30:00'

date_format = '%Y-%m-%d %H:%M:%S'

date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

difference_seconds = abs((date2 - date1).total_seconds())

print (difference_seconds)