# from customer import Customer
from bank import Bank
import csv
from transaction import Transaction 
from termcolor import colored
class Banking():
    # selection = ['1','2','3']
    
    def __init__(self):
        print(colored(('#'*100+'\n\n\n\n\n\t\t\t\tWelcome To Banking App\n\n\n\n\n'+ '#'*100),"yellow",attrs=["blink",'underline']))
        py_bank = Bank('bank_customers.csv')
        choice = None
        # while True:
        while (choice != '3'):
            choice = Banking.main_menu()
           
            # print(type(py_bank.accounts[12].overdraft_count))
            if choice == '1': 
                print(20*'=')
                customer = py_bank.sign_in() #returns object customer
                if (customer):
                    acc_type = self.accounts_menu(customer)
                    py_bank.update_customers()
                    Banking.transaction_menu(customer,acc_type,py_bank)
            elif choice == '2':
                py_bank.create_account()
            elif choice != '3':
                print(colored('Invalid Input.','red'))
                print(20*'=')
        print('\t\tGoodBye Comeback Again!')


            # for acc in py_bank.accounts:
            #     print(acc)
        pass
    @classmethod
    def main_menu(cls):
        print(colored('1- Sign In\n2- Create Account\n3- Exit','cyan'))
        inpt = input(colored('Select (1-3): ','green'))
        print(20*'=')
        return inpt
    
    @classmethod
    def transaction_menu(cls,customer,acc_typ,bank):
        selection=None
        while selection != '4':
            print(10*'*',colored('Main Meneu','yellow'),10*'*')
            if acc_typ == '1':
                print(9*'*',colored(f'Balance: {customer.checking}','magenta'),9*'*')
            if acc_typ == '2':
                print(9*'*',colored(f'Balance: {customer.savings}','magenta'),9*'*')
            if customer.active:
                print(colored("1- Withdraw\n2- Deposit\n3- Transfer\n4- Log out",'cyan'))
                selection = input(colored('Select (1-4): ','green'))
                print(20*'=')
                if selection == '1':
                    Transaction.withdraw(customer,acc_typ)
                if selection == '2':
                    Transaction.deposit(customer,acc_typ)
                if selection == '3':
                    Transaction.transfer(customer,acc_typ,bank)
            else:
                
                print(colored("1- Deposit\n2- Log out",'cyan'))
                selection = input(colored('Select (1-2): ','green'))
                if selection == '1':
                    Transaction.deposit(customer,acc_typ)
                if selection == '2':
                    selection = '4'
            bank.update_customers()
            

    @classmethod
    def accounts_menu(cls,customer):
        
        if (customer.checking != 'None' and customer.savings != 'None'):
            print(10*"*",colored(" Accounts ",'yellow'),10*"*")
            print(colored('1- Checking Account\n2- Savings','cyan'))
            choice = input(colored('Select (1-2): ','green'))
            print(20*'=')
            while choice != '1' and choice != '2':
                print('* Invalid Input *')
                choice = input(colored('Select (1-2): ','green'))
                print(20*'=')
            return choice
        
        if (customer.checking == 'None' and customer.savings != 'None' ):
            print(10*"*",colored(" Accounts ",'yellow'),10*"*")
            print(colored('1- Open Checking Account\n2- Savings Account','cyan'))
            choice = input(colored('Select (1-2): ','green'))
            print(20*'=')
            while choice != '1' and choice != '2':
                print('* Invalid Input *')
                choice = input(colored('Select (1-2): ','green'))
                print(20*'=')
            if choice == '1':
                customer.open_sec_acc()
            return choice
        
        if (customer.checking != 'None' and customer.savings == 'None' ):
            print(10*"*",colored(" Accounts ",'yellow'),10*"*")
            print(colored('1- Checking Account\n2- Open Savings Account','cyan'))
            choice = input(colored('Select (1-2): ','green'))
            print(20*'=')
            while choice != '1' and choice != '2':
                print('* Invalid Input *')
                choice = input(colored('Select (1-2): ','green'))
                print(20*'=')
            if choice == '2':
                customer.open_sec_acc()
            return choice

        pass
    pass

Banking()
# print('############### Welcome To Banking App ###############')
# py_bank = Bank('bank_customers.csv')
# # Transaction.withdraw()
# choice = None
# while True:
#     while (choice != '3'):
#         choice = Banking.main_menu()

#         if choice == '1': 
#             user = py_bank.sign_in()
#             if (user):
#                 Banking.transaction_menu()

#         elif choice == '2':
#             py_bank.create_account()
#         elif choice != '3':
#             print('Invalid Input.')
#     print('\t\tGoodBye Comeback Again!')

    
#     for acc in py_bank.accounts:
#         print(acc)

