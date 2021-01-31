#!/usr/bin/env python3

"""Python workout dictionary exercise 15

Dislay the past week temperatures as well as the previous and subsequent dates, if available.
"""

from datetime import date, timedelta, datetime

week_temperatures = dict([("20210201", -1),
                          ("20210202", 2),
                          ("20210203", -3),
                          ("20210204", 4),
                          ("20210205", -5),
                          ("20210206", 6),
                          ("20210207", -7)])

while True:

    query_date = input("enter date in yyyymmdd format: ").strip()
    temperature = week_temperatures.get(query_date)

    if not temperature:
        print("enter date from the past week: ie. 2021021 to 20210207")
    else:
        print(f"{query_date} temperature was {temperature}")

        # Convert string to datetime via strptime so ti can perform math
        # - strptime(date_string, format) is only avalible for datetime objects: past string and convert it to datetime object
        # - strftime(format): convert any date, time, datetime object to string according to given format 
        # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

        # timedelta works on any  datetime; date; time objects
        day_minus = datetime.strptime(query_date, "%Y%m%d").date() - timedelta(days=1)

        convert_str = day_minus.strftime("%Y%m%d")
        day_minus_temperature = week_temperatures.get(convert_str)

        if day_minus_temperature:
            print(f"{convert_str} temperature was {day_minus_temperature}")

