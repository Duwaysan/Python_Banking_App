# Python Banking App
![money-money-gif](https://gifgifs.com/animations/other-animations/money/lots-of-money-gif.gif)

##  Project Description
This is a simple **banking system** implemented in Python.  
It simulates the management of customers, their checking and savings accounts, deposits, withdrawals, and transfers.  
Data is stored in a CSV file (`bank_customers.csv`) to keep the system persistent between runs. 
![banking App Interface](/assets/Screenshot_1.png)



## Technologies Used
- **Python 3.x**
- **CSV module** for reading/writing customer data
- **OOP (Classes & Objects)** for `Bank`, `Customer`, `Transactions`, and `Banking`
- **Git & GitHub** for version control and commits
- **CLI (Command Line Interface)** for user interaction
- **Termcolor** for terminal color customization

---
## Installation
```bash
git clone https://github.com/Duwaysan/Python_Banking_App.git
cd Python_Banking_app.git
python3 Banking.py
```

## App Functionality

| Feature             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Create Customer     | Add new customers with checking/savings accounts or both.                          |
| Deposit             | Deposit money into checking or savings accounts.                           |
| Withdraw            | Withdraw money with balance and overdraft checks.                          |
| Transfer            | Transfer money between personal/customer accounts.                                           |
| Save to CSV         | Persist all customer data to `bank_customers.csv`.                         |
| Load from CSV       | Load existing customers and balances at startup.                           |
| Inactive Accounts   | Handle customers that are flagged as inactive.                             |
| Overdraft Count     | Track overdrafts for customers with insufficient funds.                    |


## Challenges & Key Takeaways
- **CSV Parsing**: Handling `"None"` values properly (for accounts without balances).  
- **Data Types**: Converting string values from CSV to integers/booleans safely.  
- **OOP Design**: Separating logic into multiple classes (`Customer`, `Bank`, `Transactions`).  
- **Error Handling**: Preventing crashes when data was missing, empty, or invalid.  
- **Persistence**: Ensuring changes in balances/accounts are saved back correctly to CSV.  

**Takeaway**: Learned the importance of clean class design, input validation, and handling edge cases like negative balances and missing accounts.

## ❄️ IceBox Features (Future Work)
- Log in using username
- Add transaction history for each account.  
- Create a GUI interface using HTML, CSS, and JS.  
- Use a database (SQLite/MySQL) instead of CSV for scalability.  
