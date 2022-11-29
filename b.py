class Bank:
    amount = 0

    def __init__(self, amount) -> None:
        self.amount = amount

    def menus(self):
        menusString = '''
        Enter your choice:
            1. Deposit
            2. Withdraw
            3. Display
            4. Exit
        '''
        i = int(input(menusString))
        if i == 1:
            self.deposit()
        elif i == 2:
            self.withdraw()
        elif i == 3:
            self.display()
        else:
            self.exit()

    def deposit(self):
        depoA = int(input('Enter deposit amount: ').replace(',', ''))
        self.amount += depoA
        self.menus()

    def withdraw(self):
        wdA = int(input('Enter withdraw amount: ').replace(',', ''))
        if self.amount < wdA:
            print('Withdraw can\'t be process due to your balance is low')
        else:
            self.amount -= wdA
        self.menus()

    def display(self):
        print(f"Your current amount: {format (self.amount, ',d')}")
        self.menus()

    def exit(self):
        print('Exit')

bank = Bank(0)
bank.menus()
