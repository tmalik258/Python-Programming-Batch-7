class BankBalance:
    balance = 0
    
    def __init__(self, an):
        self.account_number = an
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount has been deposited {amount}')
    
    def withdraw(self, amount):
        result = self.balance - amount
        
        if result < 0:
            self.balance = 0
        else:
            self.balance = result
        print(f'Amount has been withdrawn {amount}')
    
    def check_balance(self):
        print(f'Remaining balance is {self.balance}')


obj1 = BankBalance('fadk3543298gvj')

# talha.check_balance()

# talha.deposit(234)
# talha.check_balance()

# talha.withdraw(34)
# talha.check_balance()

# talha.withdraw(205)
# talha.check_balance()


def menu():
    print('Main Menu')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check Balance')
    print('4. Exit')
    
    try:
        option = int(input('Enter an option: '))
    except ValueError:
        print('Enter an integer\n')
        return menu()
    
    if option == 1:
        amount = float(input('Enter the amount to be deposited: '))
        obj1.deposit(amount)
    elif option == 2:
        amount = float(input('Enter the amount to be withdrawn: '))
        obj1.withdraw(amount)
    elif option == 3:
        obj1.check_balance()
    elif option == 4:
        exit(1)
    else:
        print('Invalid option')
    
    print('\n')
    
    return menu()


menu()