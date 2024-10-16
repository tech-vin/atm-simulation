pin = 1234
balance = 1000.00
transaction = []

def displayMenu():
    menu = '''
    Please Select
    1. Withdrawl        2. Change Pin
    3. View Balance     4. Mini Statement
    5. Deposit          6. Exit
    '''
    return menu

def withdraw(amount):   
    global transaction, balance
    if amount <= 0:
        return "Amount must be positive"
    if amount > balance:
        return "Insufficient balance"

    balance -= amount
    transaction.append(f'Amount debited: {amount:.2f}')
    return f'Withdrawl Successful! Remaining Balance: {balance:.2f}'

def deposit(amount):
    global transaction, balance
    if amount <= 0:
        return 'Amount must be positive'
    balance += amount
    transaction.append(f'Amount credited: {amount:.2f}')

    return f'Deposit Successful! Updated Balance: {balance:.2f}'

def changePin(enteredPin):
    global pin
    if enteredPin == pin:
        return "Pin cannot be same"
    else:
        pin = enteredPin
    return pin

def viewBalance():
    global balance
    return f'Existing balance: ${balance:.2f}'

def authenticate(enteredpin):
    return enteredpin == pin

def miniStatement():
    if not transaction:
        return "No Transactions"
    return "\n".join(transaction)


def main():
    print("Welcome to the ATM");
    enteredPin = int(input("Enter the Pin: "))
    if authenticate(enteredPin):
        print("Successfully Authenticated!")
        while True:
            print(displayMenu())
            choice = int(input("Enter Choice: "))
            if choice == 1:
                wamt = float(input("Enter Amount: "))
                print(withdraw(wamt))
            elif choice == 2:
                newpin = int(input("Enter new pin: "))
                print(changePin(newpin))
            elif choice == 3:
                print(viewBalance())
            elif choice == 4:
                print(miniStatement())
            elif choice == 5:
                damt = float(input("Enter Amount: "))
                print(deposit(damt))
            elif choice == 6:
                print("Thank you for using ATM")
                break;
            else:
                print("invalid choice")

    else:
        print("Incorrect pin")


if __name__ == "__main__":
    main()

