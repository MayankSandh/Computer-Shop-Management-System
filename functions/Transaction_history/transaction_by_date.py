# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:13:54 2021

@author: Tanmay
"""

def transaction_by_date():
    print("\033c")
    t = input('Enter the date here (dd/mm/yyyy): ')
    for i in range(len(t)):
        if t[i] in ("\\", "/", "."):
            t = t[:i]+"-"+t[i+1:]
    print("\nList of the Transactions that occcured on",t,"are:")
    print("~"*60)
    print('{:<30s}{:<10s}'.format('Name of customer','Transaction ID'))
    print("~"*60)
    with open('transactions\List_of_transactions.txt','r') as rfile:
        lines = rfile.readlines()
        for j in lines:
            trid = j.rstrip('\n')
            if trid != "":
                with open('transactions/{}.txt'.format(trid),'r') as trfile:
                    memo = trfile.readlines()
                    line1 = memo[3].rstrip('\n').split('|')
                    date = line1[1].strip(' ')
                    if date == t:
                        line = memo[2].rstrip('\n').split(':')
                        name =line[1].strip(' ')
                        print('{:<30s}{:<10s}'.format(name,trid))
    print("~"*60)
    if input('\nDo you want to try another date?(y/n): ').lower()=='y':
        transaction_by_date()
    else:
        pass


