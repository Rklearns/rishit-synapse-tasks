request_spending = {
     "Mahek": { "balance": 3000.00,
        "transactions": [ {"amount": -9000.00, "category": "Creatives"},
                                  {"amount": 7000.00, "category": "Sponsor"}, 
                                  {"amount": -2000.00, "category": "Prize-Money"}, ],
                                    }, 
    "Arham": { "balance": 5000.00, 
        "transactions": [ {"amount": 8000.00, "category": "Stalls"}, 
                         {"amount": 7500.00, "category": "Seminars"}, ], },

    "Unnati": { "balance": 3500.00, 
               "transactions": [ {"amount": -5000.00, "category": "Attraction"},
                                 {"amount": 2500.00, "category": "Promo"},
                                 {"amount": -900.00, "category": "Lighting"}, 
                                 {"amount": -3000.00, "category": "Games"}, ], }, 
                                 
    "Gaurang": { "balance": 2000.00, 
           "transactions": [ {"amount": -1500.00, "category": "Website"}, 
                             {"amount": -1000.00, "category": "C2C"},
                             {"amount": -500.00, "category": "Posters"}, ], }, }

def total_spending(request_spending, account_id: str, category: str): 
    transactions = request_spending[account_id]
    for a in transactions['transactions']:#this means iterating over inside the transactions of the dictionary
        if a['category'] == category:#inside transactions checking which category is there
            return a['amount']

def account_balance(request_spending, account_id: str):
    
    account = request_spending.get(account_id)#first acccessing the acount id
    balance = account.get('balance')# in that account id accessing the balance
    transactions = account.get('transactions')#in that account accessing the transactions
    
    for b in transactions:
        balance =balance+ b['amount']
    
    return balance

def money_owed(request_spending, account_id: str):
    account=request_spending[account_id]#accesing the account id
    initial_balance=account['balance']#accessing the initial balance
    
    finalbalance = account_balance(request_spending, account_id)#final balance is bascially initial plus other transactions
    balance=finalbalance-initial_balance
    
    if balance < 0:#since if balance is negative that means money is owed therefore that positive 
        #amount has to be transferred to the acount
        udhaar = -balance
    else:
        udhaar = 0.0
    
    return udhaar



print("Total spending of Arham in stalls category is:",total_spending(request_spending, "Arham", "Stalls"))  
print("Account blance of Arham is:",account_balance(request_spending, "Arham"))              
print("Money owed to Arham is:",money_owed(request_spending, "Arham"))

