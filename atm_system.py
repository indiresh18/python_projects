class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self):
        entered_pin = input("Enter PIN: ")
        return entered_pin == self.pin

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def change_pin(self):
        current_pin = input("Enter current PIN: ")
        if current_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully.")
            else:
                print("PIN mismatch.")
        else:
            print("Incorrect current PIN.")


def display_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")


def atm_system():
    atm = ATM("1234", 5000)

    print("Welcome to ATM")

    if not atm.check_pin():
        print("Invalid PIN.")
        return

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.deposit()
        elif choice == "3":
            atm.withdraw()
        elif choice == "4":
            atm.change_pin()
        elif choice == "5":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice.")


atm_system()