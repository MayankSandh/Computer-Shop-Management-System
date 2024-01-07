# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:21:53 2021

@author: Tanmay
"""

def transaction_by_name():
    print("\033c")
    t = input("Enter the name here: ")
    print("\nList of the Transactions made by",t,"are:")
    print("~"*70)
    print('{:<25s}{:<25s}{:<10s}'.format('Transaction ID','Date of Purchase', 'Time of Purchase'))
    print("~"*70)
    with open('transactions\List_of_transactions.txt','r') as rfile:
        lines = rfile.readlines()
        for j in lines:
            trid = j.rstrip('\n')
            if trid != "":
                with open('transactions/{}.txt'.format(trid),'r') as trfile:
                    memo = trfile.readlines()
                    line = memo[2].rstrip('\n').split(':')
                    name =line[1].strip(' ')
                    line1 = memo[3].rstrip('\n').split('|')
                    date = line1[1].strip(' ')
                    time = line1[2].strip(' ')
                    if name == t:
                        print('{:<25s}{:<25s}{:<10s}'.format(trid,date,time))
    print("~"*70)
    if input('\nDo you want to try name?(y/n): ').lower()=='y':
        transaction_by_name()
    else:
        pass
