#!/usr/bin/env python3

"""Envelope class to send letter."""

class Envelope():
    """Envelope class."""

    # class attribute
    postage_multiplier = 10

    def __init__(self, weight, was_sent=False):
        self.weight = weight
        self.postage = 0
        self.was_sent = was_sent

    def send(self):
        if self.postage_needed() <= 0:
            self.was_sent = True

    def add_postage(self, another_postage):
        self.postage += another_postage

    def postage_needed(self):
        # Uses self.postage_multiplier, rather than Envelope.postage_multiplier, to get the class attribute from the *correct class*
        return (self.weight*self.postage_multiplier) - self.postage  

class BigEnvelope(Envelope):
    """Inheritance of Envelope class."""

    # overwrite class attribute
    postage_multiplier = 15

    def __init__(self, weight, was_sent=False):
        # Implicitly invoking Envelope.__init__ via super()
        super().__init__(weight, was_sent)

if __name__ == "__main__":
    # base class
    e = Envelope(1)
    e.add_postage(5)
    e.add_postage(4)
    e.send()
    print(f"small envelope current weight: {e.postage}")
    print(f"small envelope current weight: {e.was_sent}")

    e.add_postage(1)
    e.send()
    print(f"small envelope current weight: {e.postage}")
    print(f"small envelope current weight: {e.was_sent}")

    # inheritance
    big = BigEnvelope(1)
    big.add_postage(5)
    big.add_postage(4)
    big.add_postage(2)
    e.send()
    print(f"big envelope current weight: {big.postage}")
    print(f"big envelope current weight: {big.was_sent}")
