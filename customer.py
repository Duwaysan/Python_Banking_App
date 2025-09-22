
class Customer():
    def __init__(self, id, first_name, last_name,
                  password, checking=None, savings=None,
                  active = True, overdraft_count=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking = checking
        self.savings = savings
        self.active = active
        self.overdraft_draft = overdraft_count
        pass

    def __str__(self):
        return  f"""Customer[{self.id}] {self.first_name} {self.last_name}
          Active: {self.active}, Overdrafts: {self.overdraft_draft}
          Checking: {self.checking}, Savings: {self.savings}"""
    