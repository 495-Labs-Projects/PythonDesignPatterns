from wrong_payment_class import *
from abc import abstractmethod

class PaymentAdapterInterface:
	@abstractmethod
	def pay(self, amount):
		pass

	@abstractmethod
	def activity(self):
		pass

class PayPalAdapter(PaymentAdapterInterface):
	def __init__(self, paypal):
		self.__paypal = paypal

	def pay(self, amount):
		self.__paypal.send_payment(amount)

	def activity(self):
		activity = self.__paypal.deposits()
		activity.extend(self.__paypal.withdrawals())
		return activity

class VenmoAdapter(PaymentAdapterInterface):
	def __init__(self, venmo):
		self.__venmo = venmo

	def pay(self, amount):
		self.__venmo.make_payment(amount)

	def activity(self):
		return self.__venmo.account_activity()


paymentMethod1 = PayPalAdapter(PayPalAPI(1234))
paymentMethod1.pay(102)
activity1 = paymentMethod1.activity()
print(activity1)

paymentMethod2 = VenmoAdapter(VenmoAPI("rahuang"))
paymentMethod2.pay(103)
activity2 = paymentMethod2.activity()
print(activity2)

