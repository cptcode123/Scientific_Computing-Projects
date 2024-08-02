class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = self.name.center(30, '*')
        main = []
        for item in self.ledger:
            if len(item['description']) < 23:
                space_width = 30 - (len(item['description']) + len(str(item['amount'])))
                main.append(f'{item["description"]}' + ' ' * space_width + f'{item["amount"]}')
            else:
                space_width = 7 - len(str(item['amount']))
                main.append(f'{item["description"][:23]}' + ' ' * space_width + f'{item["amount"]}')
        
        total = f'Total: {self.get_balance()}'
        return title + '\n'+'\n'.join(main) + '\n' + total
    
    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])

    def check_funds(self, amount):
        return amount < self.get_balance()

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': float(amount), 'description': description})
        return
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True    
        return False
    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other.name}')
            other.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    

def create_spend_chart(categories):
    pass

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)