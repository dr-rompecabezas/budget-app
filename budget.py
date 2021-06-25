class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        return f'*************{self.category}*************'

    def deposit(self, amount, description=''):
        amount = amount
        self.ledger.append({"amount": amount, "description": description})
        # print(self.ledger)

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            neg_amount = amount * -1
            self.ledger.append({"amount": neg_amount, "description": description})
            return True
        else:
            return False
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        # print(self.category, self.ledger)
        return total

    def transfer(self, amount, transfer_category):
        transfer_to_description = 'Transfer to ' + str(transfer_category.category)
        transfer_from_description = 'Transfer from ' + str(self.category)
        if self.check_funds(amount):
            self.withdraw(amount, transfer_to_description)
            transfer_category.deposit(amount, transfer_from_description)
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

# def create_spend_chart(categories):
