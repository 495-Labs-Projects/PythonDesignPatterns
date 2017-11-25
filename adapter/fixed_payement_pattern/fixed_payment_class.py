from api import *
from abc import abstractmethod

# This includes the adapter design pattern's way of fixing the problems. 
# In this case instead of having the client code directly interact with the
# api's we have another layer of abstraction called the adapters. This way, with
# whatever payment api, our adapter will adapt that api to the expected interface
# in order for our client code to use.


# This is a PaymentAdapterInterface that defines all the functionality that the adapter
# should have when the client uses it. So in this case, any client that uses this adapter
# should be able to pay some amount and get the past activity. The whole purpose of the adapter
# is to adapt any specific api to a general interface (in this case the PaymentAdapterInterface)
# so that clients will be able to have a consist interface to work with.

class PaymentAdapterInterface:
	@abstractmethod
	def pay(self, amount):
		pass

	@abstractmethod
	def activity(self):
		pass


# This is the concrete adapter that is used for the PayPal API.
# It takes in a paypal api object to use and then actually implements the pay and activity
# methods. Therefore all the code that is needed to achieve the outcome of pay and activity
# will be wrapped in the respective function, which means the client code doesn't need to
# worry about the implementation details at all. The client code will just have to utilize this
# adapter.

class PayPalAdapter(PaymentAdapterInterface):
	def __init__(self, paypal):
		self.__paypal = paypal

	def pay(self, amount):
		self.__paypal.send_payment(amount)

	def activity(self):
		activity = self.__paypal.deposits()
		activity.extend(self.__paypal.withdrawals())
		return activity

# The same goes for the venmo adapter, and notice how we changed the pay and activity methods
# do to the same thing but with the venmo api.

class VenmoAdapter(PaymentAdapterInterface):
	def __init__(self, venmo):
		self.__venmo = venmo

	def pay(self, amount):
		self.__venmo.make_payment(amount)

	def activity(self):
		return self.__venmo.account_activity()



