# api.py
# This is just some imaginary API wrappers for paypal and venmo (two different payment methods)
# Each of the classes have different methods that may or may not do the same or similar things.
# Note: Venmo's account_activity is equivalent to the union of Paypal's deposits and withdrawals

class PayPalAPI:
  def __init__(self, account_id):
    # Some Constructor
    pass

  def deposits(self):
    deposits = []
    # Some code to retrieve all deposit activity
    # which is a list of deposits (positive amounts)
    return deposits

  def withdrawals(self):
    withdrawals = []
    # Some code to retrieve all deposit activity
    # which is a list of withdrawals (negative amounts)
    return withdrawals

  def send_payment(self, amount):
    # Some payment code
    print("Payment of $" + str(amount) + " has been sent.") 


class VenmoAPI:
  def __init__(self, username):
    # Some Constructor
    pass

  def account_activity(self):
    activity = []
    # Some code to retrieve account activity
    # which is a list of deposits (+) and withdrawals (-) amounts
    return activity

  def make_payment(self, amount):
    # Some payment code
    print("Payment of $" + str(amount) + " has been made.")

