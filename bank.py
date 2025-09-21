import csv
from customer import Customer
class Bank():
    fieldnames = ["id","first_name", "last_name", "password", "checking", "savings", "active", "overdraft_count"]

    def __init__(self, path):
        self.accounts = []
        self.load_bank(path)
        pass

    def load_bank(self,path):
        try: 
            with open(path, "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    self.accounts.append(Customer(**row)) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
        except csv.Error as e:
            print(e)
    pass