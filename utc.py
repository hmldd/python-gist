# coding:utf-8

from datetime import datetime, timedelta, date, time

# Current UTC timestamp
now_timestamp = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()
print(int(now_timestamp))

# Current local timestamp
local_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
print(int(local_timestamp))

# diff of local and utc timestamp
print(int(local_timestamp - now_timestamp))

# Get UTC midnight timestamp of today
midnight_timestamp = (datetime.combine(date.today(), time.min) - datetime(1970, 1, 1)).total_seconds()
print(int(midnight_timestamp))

# Get UTC midnight timestamp of yesterday
yesterday_midnight = midnight_timestamp - timedelta(days=1).total_seconds()
print(int(yesterday_midnight))

# Get UTC midnight timestamp from date string
midnight_timestamp = (datetime.combine(datetime.strptime("2017-08-09", "%Y-%m-%d"), time.min) - datetime(1970, 1, 1)).total_seconds()
print(int(midnight_timestamp))
