# from customer import Customer
from bank import Bank
import csv
# from transaction import Transaction 
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
                    user = py_bank.sign_in()
                    if (user):
                        Banking.transaction_menu()

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
    def transaction_menu(cls,):
            print(10*'*',f'Welcome',10*'*')
            print('1- Withdraw')
            print('2- Deposit')
            print('3- Transfer')
            print('4- Log out')
            return input('Select (1-4): ')
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

