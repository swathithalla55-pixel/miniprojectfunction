
balance = 10000

def check_balance():
    print("Available Balance: ", balance)

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))

    if amount <= 0:
        print("Invalid amount! Enter a positive amount.")
    else:
        balance += amount
        print("Amount deposited successfully!")
        print("Current Balance: ₹", balance)

def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid amount! Enter a positive amount.")
    elif amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Amount withdrawn successfully!")
        print("Current Balance: ₹", balance)

def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
