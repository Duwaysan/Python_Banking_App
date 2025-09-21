
class Customer():

    def __init__(self, id, first_name, last_name,
                  password, checking, savings,
                  active, overdraft_count):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking = checking
        self.savings = savings
        self.active = active
        self.overdraft_draft = overdraft_count

        pass