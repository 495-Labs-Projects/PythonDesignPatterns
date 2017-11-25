from api import *

# This file contains the problematic client code utilizing the two different methods of payment.
# All we are doing for both methods of payment is to send $100 and then get the account 
# activity (which should be [] since our api.py file is just boiler plate code)
# 
# Problems
# The following are some problems that occur when just directly utilizing the paypal and venmo api
#   - As a client we actually have to care about the specific implementations of each payment method
#   - If PayPal one day decides to rename their send_payment method to pay_amount, then we need to change
#	  all the places that we use that method in our client code
#	- If we ever switch from paypal to venmo, we also need to change all the implementation details
#	  of how to get the account_activity
#   - There's just a lot of changes that need to be made in a lot of different places if at any time
#	  there are any changes to the api or if we switch to another api to do the same things
#
# Note: This is also really bad for coding boundaries since we don't have a single point where our client code
# interacts with "other code" (aka the api's). This is really not clean code practice and can be very dangerous
# when any changes are made. 

paymentMethod1 = PayPalAPI(1234)
paymentMethod1.send_payment(100)
activity1 = paymentMethod1.deposits()
activity1.extend(paymentMethod1.withdrawals())
print(activity1)

paymentMethod2 = VenmoAPI("rahuang")
paymentMethod2.make_payment(101)
activity2 = paymentMethod2.account_activity()
print(activity2)
