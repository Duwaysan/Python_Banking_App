# from customer import Customer
from bank import Bank
import csv
from transaction import Transaction 
class Banking():
    selection = ['1','2','3']

    def __init__(self):
        print('############### Welcome To Banking App ###############')
        py_bank = Bank('bank_customers.csv')
        # Transaction.withdraw()
        choice = None
        while True:
            while (choice != '3'):
                choice = Banking.main_menu()

                if choice == '1': 
                    customer = py_bank.sign_in()
                    if (customer):
                        acc_type = self.accounts_menu(customer)
                        # print(customer.savings,'line 21')
                        # customer.savings += 500
                        # print(py_bank.accounts[-1],'line 23')
                        # print(customer,'line 24')
                        py_bank.update_customers()
                        
                        Banking.transaction_menu(customer,acc_type)

                elif choice == '2':
                    py_bank.create_account()
                elif choice != '3':
                    print('Invalid Input.')
            print('\t\tGoodBye Comeback Again!')


            for acc in py_bank.accounts:
                print(acc)
        pass
    @classmethod
    def main_menu(cls):
        print('1- Sign In')
        print('2- Create Account')
        print('3- Exit')
        return input('Select (1-3): ')
    
    @classmethod
    def transaction_menu(cls,customer,acc_typ):
            print(10*'*',f'Welcome',10*'*')
            print('1- Withdraw')
            print('2- Deposit')
            print('3- Transfer')
            print('4- Log out')
            selection = input('Select (1-4): ')
            if selection == '1':
                print(30*'=')
                Transaction.withdraw(customer,acc_typ)
    @classmethod
    def accounts_menu(cls,customer):
        
        if (customer.checking != 'None' and customer.savings != 'None'):
            print(10*"*","Accounts",10*"*")
            print('1- Checking Account\n2- Savings')
            choice = input('Select (1-2): ')
            while choice != '1' and choice != '2':
                print('* Invalid Input *')
                choice = input('Select (1-2): ')
            return choice
        
        if (customer.checking == 'None' and customer.savings != 'None' ):
            print(10*"*"," Accounts ",10*"*")
            print('1- Open Checking Account\n2- Savings Account')
            choice = input('Select (1-2): ')
            while choice != '1' and choice != '2':
                print('* Invalid Input *')
                choice = input('Select (1-2): ')
            if choice == '1':
                customer.open_sec_acc()
            return choice
        
        if (customer.checking != 'None' and customer.savings == 'None' ):
            print(10*"*","Accounts",10*"*")
            print('1- Checking Account\n2- Open Savings Account')
            choice = input('Select (1-2): ')
            while choice != '1' and choice != '2':
                print('* Invalid Input *')
                choice = input('Select (1-2): ')
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

