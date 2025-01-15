# Simple Banking System

# Initial balance
balance = 1000.0


# Function to check balance
def check_balance():
    print("\nYour current balance is: $", balance)


# Function to deposit money
def deposit():
    global balance
    amount = float(input("\nEnter amount to deposit: $"))
    balance += amount
    print("Successfully deposited $", amount)
    check_balance()


# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("\nEnter amount to withdraw: $"))
    if amount > balance:
        print("Insufficient funds! Your balance is only $", balance)
    else:
        balance -= amount
        print("Successfully withdrew $", amount)
        check_balance()


# Main menu loop
def main():
    while True:
        print("\n==== Simple Banking System ====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


# Run the banking system
main()
