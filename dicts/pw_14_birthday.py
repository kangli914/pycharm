#!/usr/bin/env python3

from datetime import date

birth_dates = dict([
    ("david", date(1970, 10, 1)),
    ("max", date(2008, 10, 5))])


while True:
    name = input("name: ").strip().lower()
    date_value = birth_dates.get(name)

    # exit when empty string - python conventions for checking empty 
    if not name:
        print("exit...")
        break

    # value is None
    if not date_value:
        print(f"person {name} does not exist in the database")
    else:
        # today is datetime.date object
        today = date.today()

         # (today - date_value) is 'datetime.timedelta' object
        print(f"{name} was born on {date_value.isoformat()} and is {(today - date_value).days} days old")
