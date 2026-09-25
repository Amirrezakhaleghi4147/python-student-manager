class Bank_account :

    def __init__(self, owner_name, amount) :

        self.name = owner_name
        self.amount = amount

    def withdraw(self, withdraw_amount) :
    
        self.withdraw_amount = withdraw_amount
        
        if self.withdraw_amount > self.amount : 

            raise ValueError('you dont have the budget for getting this much money ! ')

        self.amount = self.amount - self.withdraw_amount

        return self.amount


    def deposit(self, deposit_amount) :

        self.deposit_amount = deposit_amount

        self.amount = self.amount + self.deposit_amount

        return self.amount

try :

    person_1 = Bank_account('amirreza', 1000)

    print(person_1.amount)

    print(person_1.withdraw(1000))

    print(person_1.amount)

except ValueError as e :

    print(f'Error: {e}')