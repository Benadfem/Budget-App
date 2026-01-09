
#show the balance at the opening
balance = 0
def show_balance():

    if balance <= 0:
        print("******************")
        print(f"Your balance ${balance:.2f} is low deposit to your account ")
        print("******************")

    else:
        print(f"Your balance is ${balance:.2f}")
def deposit():
    print("*****************")
    amount = float(input("Enter amount to deposit: "))
    print("*****************")

    if amount <=0 :
        print("*****************")
        print("You cannot deposit amount less than zero")
        print("*****************")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    if amount >balance :
        print("*****************")
        print("Insufficient funds!")
        print("*****************")
        return 0
    elif amount < 0 :
        print("*****************")
        print("You cannot withdraw amount less than zero")
        print("*****************")
        return 0
    else:
        return amount


def main():

    global balance
    while True:
        print("*****************")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*****************")
        choice = input("Enter your choice: ")
        # if choice == "1":
        #    show_balance()
        # elif choice == "2":
        #     balance += deposit()
        # elif choice == "3":
        #     balance -= withdraw()
        # elif choice == "4":
        #     break
        # else:
        #     print("*****************")
        #     print("You Entered Invalid Choice")
        #     print("*****************")
        match choice:
            case "1":
                show_balance()
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw()
            case "4":
                break
            case _:
                print("*****************")
                print("You Entered Invalid Choice")
                print("*****************")

    print("*****************")
    print("Bye and Have a nice day!")
    print("*****************")
if __name__ == "__main__":
    main()