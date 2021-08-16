#!/usr/bin/env python3

"""A simple phone calss."""

class Phone():

    def __init__(self):
        pass

    def dial(self, number):
        print(f"Phone dailing {number}")

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()

    def run_app(self, app_name):
        return (f"SmartPhone running app: {app_name}")

class IPhone(SmartPhone):
    def __init__(self):
        super().__init__()

    def run_app(self, app_name):
         app = super().run_app(app_name).lower()
         print(app)



if __name__ == "__main__":
    phone = Phone()
    phone.dial("647-188-1821")


    iphone = IPhone()
    iphone.run_app("YOUTUBE APP")