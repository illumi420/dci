from csv_projects_funcs import csvToDictsList
import random


dict_list = csvToDictsList('transaction_data.csv')

print("Transactions: ")
print()
for transaction in dict_list:
    for key, value in transaction.items():
        print(key, value)
print()

total_spent = 0
counter = 0
dates = []
for i in dict_list:
    for l in i:
        dates.append(l)
        total_spent += float(i[l]["amount"])
        counter += 1

print(f" Total Amount: {total_spent}\n Average Amount: {total_spent/counter}\n Total Transactions: {counter}")
print()

random_transaction = random.choice(dates)       

for i in dict_list:
    for key,value in i.items():
        if key == random_transaction:
            print(f" On this Day {random_transaction} {value}")
    
