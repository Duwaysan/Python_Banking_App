import csv
from customer import Customer

class Bank():
    fieldnames = ["id","first_name", "last_name", "password", "checking", "savings", "active", "overdraft_count"]
    id = 0

    def __init__(self, path=None):
        self.accounts = []
        self.next_id = 1
        if path:
            self.from_csv(path)
        pass
    
    import csv

    def update_customers(self, filename="bank_customers.csv"):
        fieldnames = ["id", "first_name", "last_name", "password",
                      "checking", "savings", "active", "overdraft_count"]

        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows([cust.to_dict() for cust in self.accounts])

    def from_csv(self,path):
        try: 
            with open(path, "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    row.pop("id", None)  # drop id to insert mine
                    self.accounts.append(Customer(self.next_id, **row))
                    self.next_id += 1
                    # self.accounts.append(Customer(1,**row[1:])) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
        except csv.Error as e:
            print(e)
    
    def to_csv(self, customer):
        fieldnames = ["id", "first_name", "last_name", "password","checking", "savings", "active", "overdraft_count"]
        try:
            with open("bank_customers.csv", "a+",newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(customer.to_dict())
        except csv.Error as e:
            print(e)
        pass


    def create_account(self):
        id = self.accounts[-1].id +1
        first_name = input("Enter First Name: ")
        last_name = input("Enter last Name: ")
        pswrd = input("Enter Password: ")
        type_acc = -1
        checking = savings = 'None'
        while checking == 'None' and savings == 'None':
            type_acc = input('Type of Account :\n1- Checking\n2- Savings\n3- Both\nSelect (1-3): ')
            if type_acc == '3':
                checking = 0
                savings = 0
            elif type_acc == '2':
                savings = 0
            elif type_acc == '1':
                checking = 0
            else: print('Invalid Input')
        self.accounts.append(Customer(id,first_name,last_name,
                                      pswrd,checking,savings,))
        self.to_csv(self.accounts[-1])
        print(f"Account Created!! Your account ID is {id}")
        pass
    
    def sign_in(self):
        id = int(input('Account ID: '))
        password = input('Password: ')
        user = self.accounts[id-1]
        if str(user.password) == str(password):
            # print(10*'*',f'Welcome {user.first_name} {user.last_name}')
            # print('1- Withdraw')
            # print('2- Deposit')
            # print('3- Transfer')
            # print('4- Log out\nSelect (1-4): ')
            return user
        print('Your ID or Password are not correct!')
        return False

