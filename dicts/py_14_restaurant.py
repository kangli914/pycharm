#!/usr/bin/env python3

MENU = dict(tea=5, sandwich=10, burger=20)

total = 0
order = input("Entry Order: ")
# price = dict(order, None)
price = MENU.get(order, None)

while True:
    # if order is None:
    if order == "":
        break

    if price is not None:
        total += price
        print(f"{order} costs {price}, total is {total}")
    else:
        print("you order something not from the Menu")
