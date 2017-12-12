from fixed_payment_class import *

# This file contains the fixed client code utilizing the two different methods of payment.
# All we are doing for both methods of payment is to send $100 and then get the account 
# activity (which should be [] since our api.py file is just boiler plate code)
# Notice how in this version that all the iteractions are simple and direct and follow the
# adapter's interface. Also if we ever change the method of payment, we only need to change
# one line of client code.

# This solves all the problems that we have previous brought up if we instead just directly
# used the api's:
#	- As a client if we use the adapter to adapt to the payment interface that we want, the client
#	  won't need to know any sort of implementation details
#   - If PayPal one day decides to rename their send_payment method to pay_amount, then all we need to
# 	  change is just the adapter since all client code that interacts with the api uses the adapter
#	- If we ever switch from paypal to venmo, we also only need create a new venmo adapter
#   - The adapter creates a single point boundary between any client code and the "other code" (aka api)
#
# Note: Another huge advange of this code is best practices with clean code and code boundaries. We
# usually don't want to have huge amounts of direct and unauthorized interactions between client code
# and other code (which makes for an unsafe boundary). 
# Another rule of boundaries is the separations of knowns and unknowns. For example, let's say paypal,
# was still developing the api and haven't come up with the exact interface/endpoints for their api.
# In most cases we would have to wait until they are done in order for our client to directly interact
# the api. However, what we can do is create what we wished the api would do and its functionality
# in an adapter interface (similar to how we created the PaymentAdapterInterface). Then when the paypal
# api is finished, we just need to implement the PayPalAdapter and not have to change any of our client
# code to tailor to the paypal api.

# Here are some helpful links:
#   https://code.tutsplus.com/tutorials/design-patterns-the-adapter-pattern--cms-22262
#   https://gist.github.com/pazdera/1145859
#   https://www.journaldev.com/1487/adapter-design-pattern-java  

paymentMethod1 = PayPalAdapter(PayPalAPI(1234))
paymentMethod1.pay(102)
activity1 = paymentMethod1.activity()
print(activity1)

paymentMethod2 = VenmoAdapter(VenmoAPI("rahuang"))
paymentMethod2.pay(103)
activity2 = paymentMethod2.activity()
print(activity2)
