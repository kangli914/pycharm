#!/usr/bin/env python3

'''
DATABASE = dict(kangli="kangli", perfeng="perfeng")

while True:
    user = input("user name: ")

    password = DATABASE.get(user, None)
    if password is None:
        print("user not exist")
    else:
        pwd = input("password: ")
        if (pwd == password):
            print("user successfully login")
            break
        else:
            print(f"user {user} password not match")
'''

user_list = [("kli", "password1"), ("pfeng", "password2")]
DATABASE = dict(user_list)

while True:
    user = input("user name: ").strip()
    if user in DATABASE:
        pwd = input("password: ").strip()
        if pwd == DATABASE[user]:
            print("user successfully login")
            break
        else:
            print(f"{user} password not match")
    else:
        print("user not exit")
