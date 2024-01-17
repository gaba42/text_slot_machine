import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# symbols in a wheel/COLS
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

# outcome of slot machine
# generate items in slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    
    columns = []
    # generate a column for every column there is
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copy all_symbols 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns


def print_slot_machine(columns):
    # transpose
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:  # maximum index to have access to shark film
                print(column[row], "|")
            else:
                print(column[row])



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # check amount is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

# collect bet from user


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines 


# amount of bet for each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            # check the bet is betwen min and max bet amount
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    
    return amount
    


def main():
    balance = deposit()
    lines = get_number_of_lines()
    # check for invalid bet
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")



main()