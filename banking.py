# from customer import Customer
from bank import Bank
import csv
# from transaction import Transaction 
# class Banking():

#     def __init__(self):
#         print('############### Welcome To Banking App ###############')
#         self.py_bank = Bank('bank_customers.csv')

#         pass
#     pass
print('############### Welcome To Banking App ###############')
py_bank = Bank('bank_customers.csv')
# Transaction.withdraw()
choice = None
while True:
    while (choice != '3'):
        print('1- Sign In')
        print('2- Create Account')
        print('3- Exit')
        choice = input('Select (1-3): ')
        if choice == '1': 
            user = py_bank.sign_in()

        elif choice == '2': py_bank.create_account()
        elif choice != '3': print('Invalid Input.')
    print('\t\tGoodBye Comeback Again!')

    
    for acc in py_bank.accounts:
        print(acc)

    choice = None
