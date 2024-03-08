#Oluwaseun as the group leader started with the import command,  variables, for loop,greetings, Open Account & Transfer
# This program simulates a basic banking system for Wema Bank Plc.
# It generates a random 10-digit account number for new accounts and offers options for account opening, transfers,
# airtime purchases, internet banking, balance inquiries, and bill payments.
# Goodness worked on airtime and data, continue and logout, using variables, while loop etc. 
# Emmanuel worked utilities and check balance
print("WELCOME TO WEMA MOBILE APP")
print("1. Login already existing account \n2. Open New Account/Sign Up")
choose = int(input())
if choose == 1:
    from functions import chooselogin
    chooselogin()
elif choose == 2:
    from functions2 import choosenewsignup    
    choosenewsignup()
else:
    print("Invalid Command")
while True:
    print("Dashboard \n What would you like to do? \n1. Transfer \n2. Buy Airtime \n3. Buy Data \n4. Check Balance \n5. Utilities")
    option = int(input())
    if option == 1:
        from transferopts import transfer
        transfer()
    elif option == 2:
        from buy_airtime import airtime
        airtime()
    elif option == 3:
        from funcdata import dataopt
        dataopt()
    elif option == 4:
        p=4
        pin = int(input("Enter Transfer pin: "))
        while pin != p:
            print("Hello, your Account Balance is.....")
            break
        else:
            print("Incorrect pin")
            try_again = int(input("Enter Transfer pin: "))
    elif option == 5:
        print("1. Pay Electricity bill \n2. Subscribe DSTV \n3. Other Billers")
        ruj = int(input("Select option: "))
        if ruj == 1:
            cardnumber = int(input("Bill code: "))
            bill=11
            while cardnumber!=bill:
                howmuch=int(input("Amount:#"))
                print(f"Your #{howmuch} subscription was successful!")
                break
            else:
                print("Invalid number")
        elif ruj == 2:
            code = int(input("Bill code: "))
            bill=11
            while code!=bill:
                howmuch=int(input("Amount:#"))
                print(f"Your #{howmuch} subscription was successful!")
                break
            else:
                print("Invalid number")
        elif ruj == 3:
            biller_name=str(input("Biller name:")).capitalize()
            billcode = int(input("Bill code: "))
            bill=11
            while billcode!=bill:
                howmuch=int(input("Amount:#"))
                print(f"Your #{howmuch} subscription from {biller_name} was successful!")
                break
            else:
                print("Invalid number")
        else:
            print("Invalid Request!")
    print("Do you want to continue or logout?")
    print("1. Continue \n2. Logout")
    res=int(input("Option:"))
    if res == 1:
        res=True
        print("\nProceed to dashboard\n")
        continue
    elif res==2:
        res=False
        print("Logout successful, Goodbye")
        break
    else:
        print("Error")
    break
    continue