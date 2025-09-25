
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
        self.overdraft_count = overdraft_count
        pass

    def open_sec_acc(self):
        if self.savings == 'None':
            self.savings = 0
        elif self.checking == 'None':
            self.checking = 0
        else:
            return False
        return True
    
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "checking": self.checking,
            "savings": self.savings,
            "active": self.active,
            "overdraft_count": self.overdraft_count
        }
    
    def __str__(self):
        return  f"""Customer[{self.id}] {self.first_name} {self.last_name}
          Active: {self.active}, Overdrafts: {self.overdraft_count}
          Checking: {self.checking}, Savings: {self.savings}"""
    
    @classmethod
    def from_csv_row(cls, new_id, row: dict):
        def int_or_none(v):
            return "None" if v in (None, "", "None") else int(v)

        def int_or_zero(v):
            return 0 if v in (None, "", "None") else int(v)

        def boolean(v):
            s = (v or "True").strip().lower()
            if s in ("true", "1", "True", "TRUE"):
                return True
            if s in ("false", "0", "False", "FALSE"):
                return False

        return cls(
            id=new_id,
            first_name=row.get("first_name", "").strip(),
            last_name=row.get("last_name", "").strip(),
            password=row.get("password", ""),
            checking=int_or_none(row.get("checking")),
            savings=int_or_none(row.get("savings")),
            active=boolean(row.get("active")),
            overdraft_count=int_or_zero(row.get("overdraft_count")),
        )

    # def to_csv_row(self):
    #     """Convert the object back into a dict suitable for DictWriter."""
    #     return {
    #         "id": self.id,
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #         "password": self.password,
    #         "checking": self.checking if self.checking is not None else "None",
    #         "savings": self.savings if self.savings is not None else "None",
    #         "active": str(self.active),
    #         "overdraft_count": self.overdraft_count,
    #     }