# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:56:03 2021

@author: Tanmay
"""
import csv
from os import remove, rename

# def updateCell(filePath,name):
#         with open("{}".format(filePath), "r", newline="") as file:
#             data = [x for x in csv.reader(file)]
        
#         for j in data:
#             if j!=[]:
#                 if j[0]==name:
#                     j[3]='FIRED'
#                     break
        
#         remove("{}".format(filePath))
#         with open('abcd.csv', "a", newline="") as file:
#             writer = csv.writer(file, delimiter = ",")
#             writer.writerows(data)
#         rename('abcd.csv',"{}".format(filePath))

def deleteRow(filePath,name):
        with open('functions\\option910\\workers_list.csv', "r", newline="") as file:
            reader = csv.reader(file)
            data = [x for x in csv.reader(file)]
        ind = 0
        for j in data:
            if j!=[]:
                if j[0]==name:
                    data.pop(ind)
                    break
            ind+=1
        
        remove("{}".format('functions\\option910\\workers_list.csv'))
        with open('abcd.csv', "a", newline="") as file:
            writer = csv.writer(file, delimiter = ",")
            writer.writerows(data)
        rename('abcd.csv',"{}".format('functions\\option910\\workers_list.csv'))

    
def workerlist():
    print("\033c")
    print("~"*70)
    print("WORKERS LIST".center(70, " "))
    with open('functions\\option910\\workers_list.csv','r',newline='') as f:
            print("~"*70)
            print("{:10s}{:20s}{:20s}{:20s}".format('Sno.','NAME','SALARY','DATE HIRED'))
            print("~"*70)
            read = csv.reader(f)
            sno = 0
            for row in read:
                sno+=1
                if row!=[]:
                    print('{:10s}{:20s}{:20s}{:20s}'.format(str(sno),row[0],row[1],row[2]))
            else:
                print("~"*70)

    print()
    input("Press ENTER to continue: ")

        
def hirefireworkers():
    while True:
        print("\033c")
        print("~"*35)
        print('Enter 1 to Add workers.')
        print('Enter 2 to Remove workers.')
        print('Enter 3 to quit.')
        print("~"*35)
        hf = input("Enter the number here: ")
        if hf == '1':
            with open('functions\\option910\\workers_list.csv','a', newline="") as f:
                writer = csv.writer(f)
                new_w = input('\nEnter the name of worker here: ')
                new_s = input("Enter the salary to be given to the worker: ")
                new_d = input("Enter date of hiring(dd/mm/yyyy): ")
                for i in range(len(new_d)):
                    if new_d[i] in ("-", ".", "\\"):
                        new_d = new_d[:i]+"/"+new_d[i+1:]
                writer.writerow([new_w,new_s,new_d])
                print('List of workers updated.')    
                input("Press ENTER to continue: ") 
        elif hf == '2':
                name = input("\nEnter the name of the worker to be fired: ")
                deleteRow('workers_list.csv',name)
                print('List of workers updated.')    
                input("Press ENTER to continue: ") 
        elif hf == '3':
            break
        else:
            print("Please enter a valid option.")
            input()
