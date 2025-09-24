

class Transaction:

#     @classmethod
#     def decide_transaction(cls,selection,amount,acc_type,src, dist=None):
#         if selection == "1":
#             cls.withdraw(amount,src,acc_type)
#         elif selection == "2":
#             cls.deposit()
#         elif selection == "3" and not dist:
#             cls.transfer()


    @classmethod
    def withdraw(cls,customer,acc_typ):
            if acc_typ == '1':
                customer.checking = cls.withdraw_implem(customer,customer.checking)
            if acc_typ == '2':
               customer.savings = cls.withdraw_implem(customer, customer.savings)
        

    @classmethod
    def withdraw_implem(cls,customer,account):
        fee = 35
        max_withdrawal = 100 
        min_withdrawal = 1
        if (customer.active):
            print(f'Current Balance {account}')
            amount = int(input('Enter Withdrawal Amount: '))
            if (amount<=max_withdrawal and amount>=min_withdrawal):
                if ((account - amount - fee) < -100):
                    print(f'Insufficient funds! Withdrawal denied.\nYour Balance: {account}')
                else:
                    account -= amount
                    if (account< 0):
                        account -= fee
                        customer.overdraft_count +=1
                        if customer.overdraft_count == 2: 
                            customer.active = False
                            print(f'You have 2 overdrafts\nYour account has been decactivated!')
    
                    print(f'Withdrawal seccessful. New balance {account}')
            else:
                print('You can withdraw (1 - 100)$ !')
        else: print(f'Your account is inactive, deposit moeny to activate it')
        return account

        
    @classmethod
    def deposit(cls,customer,acc_type):
        if acc_type == '1':
            customer.checking = cls.deposit_implem(customer.checking)
        if acc_type == '2':
            customer.savings = cls.deposit_implem(customer.savings)
        if (customer.savings == 'None' or customer.savings >= 0)and ( customer.checking == 'None' or customer.checking >= 0):
            customer.overdraft_count = 0
            customer.active = True
        pass

    @classmethod   
    def deposit_implem(cls, account):
        print(f'Current Balance {account}')
        amount = int(input('Enter Deposit Amount: '))
        if (amount>0):
            account += amount
            print(f'Deposit seccessful. New balance {account}')
        else: print('You can deposit positive numbers only!')
        return account

    @classmethod
    def transfer(cls,customer,acc_type,bank):
        # if acc_type = '1':
            



        pass

    def transfer_implem(cls,customer,account,bank):
        if customer.active:
            dist_id = int(input("Enter Recipient's ID: "))
            amount = int(input("Enter Amount of money: "))
            if account < amount :
                print(f'Insufficient funds! Withdrawal denied.\nYour Balance: {account}')
            else:
                cls.check_recipient_accounts(dist_id,bank)
        else: print(f'Your account is inactive, deposit money to activate it')

    def check_recipient_accounts(self,id,bank):
        recipient = bank.accounts[id-1]
        if recipient.checking != 'None' and recipient.savings != 'None':
            print(f"Which account of {recipient.first_name} {recipient.last_name} you want to transfer to?")
            print('1- Checking Account')
            print('2- Savings Account')
            input('Select (1-2): ')



    





    # Python's CSV package will give you all you need to Create, Read, Update, Delete a CSV.
# This functionality is all you will need to be able to complete your Python Banking Project.
# The official docs are accessible here: https://docs.python.org/3/library/csv.html#

# HINT:
# Using a dictionary is a good data structure to translate into a CSV, because:
# * A list of dictionaries is similar to rows in a table
# * Each key in a dictionary can correspond to a column name

# HOW TO USE:
# 1.0 Import the csv and os packages:
import csv
import os

# 1.1 Seed Data to CSV
doctor_who_info = [
    { 'Name': 'The First Doctor',  'Actor': 'William Hartnell',  'Number of Episodes': 134 },
    { 'Name': 'The Second Doctor', 'Actor': 'Patrick Troughton', 'Number of Episodes': 119 }, 
    { 'Name': 'The Third Doctor',  'Actor': 'Jon Pertwee',       'Number of Episodes': 128 }, 
    { 'Name': 'The Fourth Doctor', 'Actor': 'Tom Baker',         'Number of Episodes': 172 }, 
    { 'Name': 'The Fifth Doctor',  'Actor': 'Peter Davison',     'Number of Episodes': 69  }
]

# 2.0 Set fieldnames once:
fieldnames = ["Name", "Actor", "Number of Episodes"]  

# 3.0 Check CSV File Exists (otherwise error thrown!)
# 3.1 Set Headers in the CSVFile 
# 3.2 SEED DATA TO CSV
# 3.3 EXAMPLE: writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# 3.4 "w" option will allow writing, but NOT appending...
if not os.path.exists("./doctor_who.csv"):
    with open("./doctor_who.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in doctor_who_info:
                writer.writerow(row)
        except csv.Error as e:
            print(e)

# 4.0 If Exists - ReadFile / Rows:
try: 
    with open("doctor_who.csv", "r") as file:
        contents = csv.DictReader(file)
        for row in contents:
            print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
            for prop in fieldnames:
                print(row[prop]) # will print the value of each individual property
except csv.Error as e:
    print(e)


# 5.0 Add Individual Row => "a+" option will allow reading and APPENDING to file
try:
    new_row = {'Name': 'The Sixth Doctor', 'Actor': 'Harrison Ford', 'Number of Episodes': 1 }
    with open("doctor_who.csv", "a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_row)
except csv.Error as e:
    print(e)


# 6.0 Updating A row
# --- There is no no way to directly update one single row using the Python CSV import module
# --- or through any other means you will have access to. This means you will have to work through 
# --- using data structures to find a way to update an individual item and rewrite the entire file.
# --- we will walk through this process in class.



# 7.0 Deleting A Row
# --- There is no no way to directly delete one single row using the Python CSV import module
# --- or through any other means you will have access to. This means you will have to work through 
# --- using data structures to find a way to delete an individual item and rewrite the entire file.
# --- we will walk through this process in class.