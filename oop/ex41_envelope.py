#!/usr/bin/env python3

"""Envelope class to send letter."""

class Envelope():
    """Envelope class."""

    def __init__(self, weight, was_sent=False):
        self.weight = weight
        self.was_sent = was_sent
        self.postage = 0

    def send(self):
        if self.postage_needed() <= 0:
            self.was_sent = True

    def add_postage(self, another_postage):
        self.postage += another_postage
        self.send()

    def postage_needed(self):
        return self.weight*10 - self.postage


class BigEnvelope(Envelope):
    """Inheritance of Envelope class."""

    def __init__(self, weight, was_sent=False):
        super().__init__(weight, was_sent)

    def postage_needed(self):
        return self.weight*15 - self.postage 

if __name__ == "__main__":
    # base class
    e = Envelope(1)
    e.add_postage(5)
    e.add_postage(4)
    print(f"small envelope current weight: {e.postage}")
    print(f"small envelope current weight: {e.was_sent}")

    e.add_postage(1)
    print(f"small envelope current weight: {e.postage}")
    print(f"small envelope current weight: {e.was_sent}")

    # inheritance
    big = BigEnvelope(1)
    big.add_postage(5)
    big.add_postage(4)
    big.add_postage(2)
    print(f"big envelope current weight: {big.postage}")
    print(f"big envelope current weight: {big.was_sent}")
