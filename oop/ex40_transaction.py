#!/usr/bin/env python3

"""Define a Transaction class, in which each instance represents either a deposit or a
withdrawal from a bank account."""


class Transaction:
	"""When creating a new instance of Transaction, you’ll need to specify an amount—positive for a deposit and negative for a withdrawal.
Use a class attribute to keep track of the current balance, which should be equal to the sum of the amounts in all instances created to date.
"""

	# Use a class attribute to keep track of the current balance
	balance = 0

	def __init__(self, amount):
		self.amount = int(amount)
		Transaction.balance += int(amount)

		if amount >= 0:
			print(f"Depsited: ${self.amount}")
		else:
			print(f"Withdrawal: ${self.amount}")
		
		print(f"current balance: {Transaction.balance}" )

if __name__ == "__main__":
	Transaction(12)
	[Transaction(amount) for amount in (3,-10,50)]
