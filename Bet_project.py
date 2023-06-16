#!/usr/bin/env python
# coding: utf-8

# # This is a simple Python code to replicate the Casino slot game

# In[ ]:


# Imports the libraries required for processing
import random 
import math


# In[40]:


# define the global constants that will be used in most of the functions
MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3
SYMBOL_COUNT={'A':2,'B':4,'C':6,'D':5}
SYMBOL_VALUE={'A':5,'B':4,'C':2,'D':3}


# In[41]:


# Use this function to get the deposit amount from the players
def deposit():
    while True:
        amount=input("Enter the amount you like to deposit : $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount")
    return amount


# In[64]:


# Main function executing the game
def main():
    balance=deposit()
    while True:
        print(f"Current balance id ${balance}")
        spin=input("press enter to spin(q to Quit).")
        if spin=="q":
            break
        balance+=game(balance)
        print(f"You left with ${balance}")
   
    


# In[57]:


# this function is called for each instance of the game . It runs until q is pressed by player
def game(balance):
    lines=get_no_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet > balance:
            print("You dont have enough to bet. Your current balance is $",balance)
        else:
            break
        
    print(f"You are betting ${bet} on {lines}lines.Total bet is equal to ${total_bet}")
    slots=get_slot_spin(ROWS,COLS,SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,SYMBOL_VALUE)
    print(f"You won ${winnings}.")
    print(f"You won on lines ",*winning_lines)
    return winnings-bet


# In[58]:


# Function to get the no of lines that user like to bet
def get_no_lines():
    
     while True:
        lines=input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+')?')
        if lines.isdigit():
            lines=int(lines)
            if lines>0 and lines <=MAX_LINES:
                break
            else:
                print("Lines must be between 1 and 3")
        else:
            print("Please enter a valid number of lines")
     return lines
    


# In[68]:


# Function to get the random slot spin 
def get_slot_spin(rows,cols,symbols):
    all_symbols=[]
    for symbols,SYMBOL_COUNT in symbols.items():
        for _ in range(SYMBOL_COUNT):
            all_symbols.append(symbols)
    columns=[]
    
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


# In[60]:


# Function to print the slot spin output
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row])


# In[61]:


# Function to get the bet amount from the user
def get_bet():
     while True:
        bet=input("What would you like to bet? ("+str(MIN_BET)+'-'+str(MAX_BET)+')?')
        if bet.isdigit():
            bet=int(bet)
            if bet>=MIN_BET and bet <=MAX_BET:
                break
            else:
                print("Bet amount must be between "+str(MIN_BET)+'-'+str(MAX_BET)+')')
        else:
            print("Please enter a valid bet amount")
     return bet
    


# In[66]:


# Function to check the winning amount for each bet
def check_winnings(cols,lines,bet,values):
    winning=0
    w_lines=[]
    for line in range(lines):
        symbol=cols[0][line]
        for col in cols:
            symb=col[line]
            if symbol!=symb:
                break
        else:
            winning+=values[symbol]*bet
            w_lines.append(line+1)
    return winning,w_lines
        
    


# In[ ]:


main()


# In[ ]:




