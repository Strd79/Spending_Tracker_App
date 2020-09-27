class Transaction:

    def __init__(self, merchant, date, amount, tag, user, id = None):
        self.merchant = merchant
        self.date = date
        self.amount = amount
        self.tag = tag
        self.user = user
        self.id = id