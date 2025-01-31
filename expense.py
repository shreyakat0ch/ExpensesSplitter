def read_expenses(file_path):
    expenses = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, amount = line.strip().split(',')
                amount = float(amount)
                if name in expenses:
                    expenses[name] += amount
                else:
                    expenses[name] = amount
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return expenses

def calculate_balances(expenses):
    total_expenses = sum(expenses.values())
    num_people = len(expenses)
    average_expense = total_expenses / num_people
    
    balances = {}
    for person, amount in expenses.items():
        balances[person] = amount - average_expense
    return balances

def print_balances(balances):
    for person, balance in balances.items():
        if balance > 0:
            print(f"{person} is owed ${balance:.2f}")
        elif balance < 0:
            print(f"{person} owes ${-balance:.2f}")
        else:
            print(f"{person} is settled up.")

def main():
    file_path = 'expenses.txt'
    expenses = read_expenses(file_path)
    if not expenses:
        return
    
    balances = calculate_balances(expenses)
    print_balances(balances)

if __name__ == '__main__':
    main()
