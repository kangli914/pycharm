#!/usr/bin/env python3

MENU = dict(tea=5, sandwich=10, burger=20)


def restaurant():
    total = 0

    while True:

        order = input("Entry Order: ").strip()

        ## if "order" is an empty string, break out of the loop 
        # if order == "":
        if not order:               # python conventions
            print(f"total is {total}")
            break

        price = MENU.get(order, None)
        if price is not None:
        # if order in MENU:
            total += price
            print(f"{order} costs {price}, total is {total}")
        else:
            print("you order something not from the Menu")


restaurant()