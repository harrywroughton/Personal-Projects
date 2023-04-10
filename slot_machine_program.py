import random

# Global variables that applies all the way throughout or needs to be changed
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Below are the symbols the slot machine with randomly generate from. Made into a dictionary.
# A is the most valuable to D being the least.
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

'''Function defined. symbols above will be passed into this to generate randomly. 
List contains all of different values that could come up.
for loop adds all of symbols into the list.
Using .itmes allows for value AND the key associated within the dictionary, rather than
for example, manually referencing the values
Second for loop uses an underscore as it is an anonymous variable - for when the count or iteration value
doesn't matter
The loop will go through the dictionary with symbol referencing to the letters, and symbol_count referencing
to the number. Then on the second for loop, the append function will, for example, recognise 'A' and add
  to the list two times.'''
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

# Columns list is defined. Then it will generate a column for every column we have. So, if we have 3 columns, 
#   it will loop through 3 times. Then inside the for loop, the purpose is to pick random values for each row
#   in the column.
    
    columns = [] 
    for col in range(cols): 
        column = [] # equal to empty list
        current_symbols = all_symbols[:] # current symbols is equal to a copy of all_symbols
        for row in range(rows): # loops through the number of values needed to generate
            value = random.choice(current_symbols) # first value is randomised from current_symbols
            current_symbols.remove(value) # then we remove the value, so as not to pick it again
            column.append(value) # now we've added the value to the column, we now have however many rows there are 
            #   inside of the column

        columns.append(column) # finally, column is added to the list

    return columns

# function below ensures slot machine will print out numbers in the style they are supposed to: i.e. as columns
#   but presented as rows. Essentially this is transposing (exchanging places = rows to cols)
def print_slot_machine(columns):
    # number of rows we have is based on the number of columns, therefore number of rows
        #   we have is based on number of elements in each of the columns. Setting at 0 assumes we have at least 
        #   one column - needs to be there for column to be accessed.
    for row in range(len(columns[0])): 
        # enumerate gives the index (e.g. 0, 1, 2, 3) as well as the item
        for i, column in enumerate (columns): 
            # len of columns - 1 is the maximum index to access an element in the columns list
            if i != len(columns) - 1: 
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

# defining the function of depositing
def deposit(): 
    while True: # setting a while loop that ensures user is directed back to function if invalid input
        amount = input("How much would you like to deposit? £") # calling the variable which will store input
        if amount.isdigit(): # isdigit will tell us amount is a number and lead to line 5
            amount = int(amount) # now amount is converted to an integer£100
            if amount > 0: # ensures user is entering a valid number
                break # should all the above criteria be met, the loop will be finished
            else:
                print("Amount must be greater than 0.") # if user types 0, they will be taken back through the loop
        else:
            print("Please enter a number.") # if user enters, e.g., a string, the following will print

    return amount # gives the amount once loop is completed

def get_number_of_lines():
    while True: # setting a while loop that ensures user is directed back to function if invalid input
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ") # user given option of number 
        # of lines from 1 - 3(MAX_LINES - declared as glocal variable in case it will be changed.) MAX_LINES converted to 
        # string to ensure it works in input
        if lines.isdigit(): # isdigit will tell us amount is a number and lead to line 5
            lines = int(lines) # now lines is converted to an integer
            if 1 <= lines <= MAX_LINES: # essentially, this checks if the input (lines) (1,2 or 3) is in between, or one of, these 
                # numbers
                break # should all the above criteria be met, the loop will be finished
            else:
                print("Enter a valid number of lines.") # if user types outside of 1 - MAX_LINES, they will be taken
                #back through the loop
        else:
            print("Please enter a number.") # if user enters, e.g., a string, the following will print

    return lines # gives the amount once loop is completed


def get_bet():
    while True: # setting a while loop that ensures user is directed back to function if invalid input
        amount = input("How much would you like to bet on each line? £") # calling the variable which will store input
        if amount.isdigit(): # isdigit will tell us amount is a number and lead to line 5
            amount = int(amount) # now amount is converted to an integer£100
            if MIN_BET <= amount <= MAX_BET: # if user enters number between MIN and MAX_BET, the loop continues
                break # should all the above criteria be met, the loop will be finished
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.") # if invalid input entered, user is asked
                # to enter number between min and max bet - f function allows variables to show in string.
        else:
            print("Please enter a number.") # if user enters, e.g., a string, the following will print

    return amount # gives the amount once loop is completed
# We now have a function that gets the deposit amount, and the number of lines


def main():
    balance = deposit() # deposit function now simplified to balance variable 
    lines = get_number_of_lines() # get_number_of_lines function simplified to lines
    while True: # while loop exists here should the user enter more money than they have for their bet on each
        # line. This will redirect back to the how much to bet question.
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough funds to bet that amount. You current balance is: {balance}")
        else:
            break
    bet = get_bet() # again, variable simplified to bet for convenience of main function
    total_bet = bet * lines # user's bet is * by their number of lines chosen
    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}") # f string allows
    # user to see their total total bet by incorporating variables

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main() # calling main function will take the program through all while loops declared above



    
