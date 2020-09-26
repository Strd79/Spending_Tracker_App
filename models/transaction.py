class Transaction:

    def __init__(self, merchant, date, amount, tag, id = None):
        self.merchant = merchant
        self.date = date
        self.amount = amount
        self.tag = tag
        self.id = id