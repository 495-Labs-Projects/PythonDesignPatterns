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


# Bad Client Code

paymentMethod1 = PayPalAPI(1234)
paymentMethod1.send_payment(100)
activity1 = paymentMethod1.deposits()
activity1.extend(paymentMethod1.withdrawals())
print(activity1)

paymentMethod2 = VenmoAPI("rahuang")
paymentMethod2.make_payment(101)
activity2 = paymentMethod2.account_activity()
print(activity2)

