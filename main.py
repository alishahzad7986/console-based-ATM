print("=================================")
print("        Welcome to Our ATM       ")
print("=================================")

cash = 500000
pin = 1234

def atm_menu():
    print("\n========== ATM MENU ==========")
    print("1) Available Balance")
    print("2) Cash Withdrawal")
    print("3) Money Deposit")
    print("4) PIN Change")
    print("5) Exit")
    print("==============================")


entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    print("Welcome Abu Turab!")

    while True:
        atm_menu()
        option = input("Enter your choice: ")

        if option == "1":
            print("Your available balance is:", cash)

        elif option == "2":
            w_amount = int(input("Enter your withdrawal amount: "))
            if w_amount <= cash:
                cash -= w_amount
                print("Withdrawal Successful!")
                print("Remaining Balance:", cash)
            else:
                print("Insufficient Balance!")

        elif option == "3":
            d_amount = int(input("Enter your deposit amount: "))
            cash += d_amount
            print("Deposit Successful!")
            print("Updated Balance:", cash)

        elif option == "4":
            new_pin = int(input("Enter New PIN: "))
            pin = new_pin
            print("PIN Changed Successfully!")

        elif option == "5":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid PIN. Access Denied.")