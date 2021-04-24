database = {}
database ["7554535648"] = "Ifeanyi", "Eze", "IE", "1234", 0



current_balance = 0
import random

def init():
    print("***** Welcome to Mybank *****")
    user = int(input("Please press one(1) to login or two(2) to register \n"))
    if  user == 1:
        login()
    elif user == 2:
        register()
    else:
        print("Invalid selection, please input correct value")
        init()

def login():
    print("===== Welcome to Mybank =====")
    user1 = (input("Please input account number \n"))
    is_valid = account_validation(user1)
    if is_valid:

        password1 = (input('Please input password \n'))

        for user_account, userpassword in database.items():
            if user1 in user_account and password1 in userpassword:
                bankoperations(userpassword)
                break
            else:
                print("Invalid account number or password, Please input right details")
                login()

def account_validation(user1):
    if user1:

        if len(str(user1)) == 10:
            try:
                int(user1)
                return True
            except TypeError:
                print("Invalid account")
                init()
                return False
            except ValueError:
                print("Invalid")
                init()
                return False
        else:
            print("Invalid account number")
            init()
    else:
        print("User validation failed")
        init()
        return False
   

def register():
    print("Welcome to Mybank, please input details ")
    first_name = input("Please input first name \n")
    last_name = input("Please input last name \n")
    email = input("Please input email address \n")
    password = input("Please create your four digit password \n")
    # current_balance = 0
     
    account_number = generate_account()
    database[account_number] = [first_name, last_name, email, password]
    print(database)
    print(f"Welcome {first_name} {last_name} to Mybank, your current balance is {current_balance} and new account number is {account_number} please keep it safe")
    login()

def generate_account():
    return random.randrange(1111111111,9999999999)

def bankoperations(user):
    print(f"Welcome, {user[1]} {user[0]}.")
    
    print('******These are the available options:******')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    
    pickedOption = int(input("Please select an option \n"))
    if pickedOption == 1:
        Withdrawal()
    elif pickedOption == 2:
        cashdeposit()
    elif pickedOption == 3:
        complaint()
   
    else:
        print("Wrong input, please input right option")
        bankoperations(user)
        

def Withdrawal(userpassword):
   print(f"Welcome {userpassword[0]} {userpassword[1]}, how much would you like to withdraw?")
   amount = int(input("Please input amount\n"))
   if amount > current_balance:
        print("Insufficient balance.")
        option = input("Click Yes if you would like to perform another transaction else, type No \n")
        if option == "Yes":
            bankoperations(userpassword)
        elif option == "No":
            logout()
   elif amount == current_balance:
       print("Thank you.")
       options = input("Click Yes if you would like to perform another transaction else, type No \n")
       if options == "Yes":
            bankoperations(userpassword)
       elif options == "No":
           print("Thank you")
           logout()


    
def cashdeposit():
    print("Welcome your current balance is 0.0")
    cash = float(input("How much would you like to deposit? \n"))
    print(f"Your current balance is {cash + current_balance}")
    another_transaction = input("Click Yes if you would like to perform another transaction, else No \n")
    if another_transaction == "Yes":
        print("Please login")
        login()

    elif another_transaction == "No":
        logout()

    else:
        print("Invalid selection, please login again")
        login()


def complaint():
    name = input("Please state your complaint\n")
    print("Thank you for your reply")
    another_transaction = input("Click Yes if you would like to perform another transaction, else No \n")
    if another_transaction == "Yes":
        print("Please login ")
        login()

    elif another_transaction == "No":
        logout()

    else:
        print("Invalid selection, please login again")
        login()

    
def logout():
    print("Please take your card.")
    exit()
def another_transactions():
    
    login()

init()