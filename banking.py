# from customer import Customer
from bank import Bank
import csv

    
print('############### Welcome To Banking App ###############')
choice = None
while (choice != '3'):
    print('\t\t     1- Sign In \t\t\t')
    print('\t\t     2- Create Account \t\t\t')
    print('\t\t     3- Exit \t\t\t')
    choice = input('\n\t\t   Enter a number: ')
    if choice == '1': print("sign in")
    elif choice == '2': print('sign up')
    elif choice != '3': print('Invalid Input.')
print('\t\tGoodBye Comeback Again!')

py_bank = Bank('bank_customers.csv')
print(py_bank.accounts[0].first_name)
