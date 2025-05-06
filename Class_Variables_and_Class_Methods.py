class Bank:
    # Class variable shared by all instances
    bank_name = "HBL Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    # Class method to change the class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Method to display bank info
    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Create instances
account1 = Bank("Rameen")
account2 = Bank("Rashid")

# Display original bank name for both instances
account1.display_info()
account2.display_info()

# Change the bank name using the class method
Bank.change_bank_name("Meezan Bank Pvt Ltd")

# Display updated bank name for both instances
account1.display_info()
account2.display_info()
