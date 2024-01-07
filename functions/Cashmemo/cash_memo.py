# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 07:01:26 2021

@author: Tanmay
"""
def cash_memo():
    found = False
    print("\033c")
    t = input("Enter your transaction id here: ")
    print("\n")
    with open('transactions/List_of_transactions.txt','r') as file0:
        rows = file0.readlines()
        for trno in rows:
            if trno.rstrip('\n')==t:
                found = True
        if found == True:
                with open("transactions/{}.txt".format(t), "r") as file:
                                    lines = file.readlines()
                                    for line in lines:
                                        print(line.rstrip('\n'))
        else:
            print('Invalid Transaction Number.')
            print('Please check the transaction number before entering.')
            cash_memo()
    if input('Do you want to try another id?(y/n): ').lower()=='y':
        cash_memo()
    else:
        pass

                            