# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:35:48 2021

@author: suprit naik
"""

import csv


def update_hardware():
    print("\033c")
    while True:
        
        file_names=["processor.csv","monitors.csv","graphics card.csv","memory chips.csv","storage.csv"]
        files=["Processor","Monitors","Graphics Card","Memory Chips","Storage",]                          #files are the names which will be shown in output
        
        choice=-1
        choice1=-1
        choice2=-1
        choice3=-1
        choice4=-1
        print()
        print("\033c") 
        print("~"*50)
        print("PRODUCT CATEGORIES")
        print("~"*50)
        print("0) Enter 0 to exit.")
        
        for k in range(len(files)):
            print((k+1),") ",files[k],sep="")
            
        print("~"*50)
        print()
        choice=int(input("Choose which option : "))
        print()
        
        
        
        if choice==0:
            break
        print("\033c")
        for n in range(len(file_names)):                                                  #n=0,1,2,3,4,5... (number of files-1)
            if choice==(n+1):
                while True:
                    print("\033c") 
                    print("~"*50)
                    print("PRODUCT CATEGORIES >>",files[n])
                    print("~"*50)
                    print("0) Enter 0 to go back")
                    print("1) To add product")
                    print("2) To update/remove product")
                    print("~"*50)
                    print()
                    if choice1 != 0:
                        choice1=int(input("Choose which option : "))
                        print()
                    else:
                        break
                    print("\033c")
                    if choice1==1:   
                        with open("hardware/{}".format(file_names[n]),"a",newline="")as file:
                            writer=csv.writer(file)
                            new_p=input("Enter the brand of the product : ")
                            new_d=input("Write the description of the product :")
                            new_pr=input("Enter the price of the product : ")
                            writer.writerow([new_p,new_d,new_pr])
                            print()
                            print("~"*50)
                            print("New product has been added.")
                            a=input("Press ENTER to continue: ")
                            file.close()
                            print("~"*50)
                            print()
                    print("\033c")       
                    if choice1==2:
                        while True:
                            infile=open('hardware/{}'.format(file_names[n]),"r")
                            read=csv.reader(infile)
                            print("\033c") 
                            print("~"*50)
                            print("PRODUCT CATEGORIES >>",files[n],">> Brand")
                            print("~"*50)
                            print("0) Enter 0 to go back")
                            sno=1
                            elist=[]                                            #elist is existing list
                            for row in read:
                                if row[0] not in elist:
                                    elist.append(row[0])
                                    print(sno,") ",row[0],sep="")
                                    sno+=1
                            print("~"*50)
                            print()
                            if choice2 != 0:
                                choice2=int(input("Choose which option : "))
                            print()
                            
                            if choice2==0:
                                break
                            print("\033c")
                            for no in range(len(elist)):
                                if choice2==no+1:
                                    while True:
                                        infile.seek(0)
                                        print("~"*50)
                                        print("\033c") 
                                        print("PRODUCT CATEGORIES >>",files[n],">> Brand >>",elist[no])
                                        print("~"*50)
                                        print("0) Enter 0 to go back")
                                        sno=1
                                        flist=[]
                                        for row in read:
                                            if row[0]==elist[no]:
                                                print("{:1d}) {:30s}".format(sno,row[1]))
                                                print("\t\t Price :-",row[2])
                                                flist.append(row)                                   #flist is the last list containg details about selected product
                                                sno+=1
                                        print("~"*50)
                                        print()
                                        if choice3 != 0:
                                            choice3=int(input("Choose which option : "))
                                        print()
                                        
                                        if choice3==0:
                                            break
                                        print("\033c")    
                                        for no in range(len(flist)):
                                            if choice3==no+1:
                                                while True:  
                                                    print("\033c")                                              
                                                    print("~"*50)
                                                    print(flist[no])
                                                    print("......>> CHANGES")
                                                    print("~"*50)
                                                    print("0) Enter 0 to go back")
                                                    print("1) To update description")
                                                    print("2) To update price")
                                                    print("3) To remove product")
                                                    print("~"*50)
                                                    print()
                                                    choice4=int(input("Choose which option : "))
                                                    print()
                                                    infile.seek(0)
                                                        
                                                    if choice4==0:
                                                        break
                                                    
                                                    read_new=[]
                                                    for row in read:
                                                        read_new.append(row)
                                                    
                                                    if choice4==3:
                                                        infile.seek(0)
                                                            
                                                        ofile=open('hardware/{}'.format(file_names[n]),"w",newline="")
                                                        writer=csv.writer(ofile)
                                                        
                                                        for row in read_new:
                                                            if row==flist[no]:
                                                                continue
                                                            writer.writerow(row)
                                                                                                                        
                                                        ofile.close()
                                                        
                                                        print("~"*50)
                                                        print()
                                                        print("Product has been removed.")
                                                        a=input("Press ENTER to continue: ")
                                                        print()
                                                        print("~"*50)
                                                        
                                                        choice4=0
                                                        choice3=0
                                                        choice2=0
                                                        choice1=0
                                                        break
                                                        
                                                            
                                                            
                                                    if choice4==1:
                                                        
                                                        n_desc=input("Write the new description for the product : ")
                                                        
                                                        ofile=open('hardware/{}'.format(file_names[n]),"w",newline="")
                                                        writer=csv.writer(ofile)
                                                                                                                
                                                        for row in read_new:
                                                            if row==flist[0]:
                                                                writer.writerow([flist[0][0],n_desc,flist[0][2]])
                                                                continue
                                                            writer.writerow(row)
                                                                                                                        
                                                        ofile.close()
                                                        
                                                        print("~"*50)
                                                        print()
                                                        print("Description has been updated.")
                                                        a=input("Press ENTER to continue: ")
                                                        print()
                                                        print("~"*50)
                                                        
                                                        choice4=0
                                                        choice3=0
                                                        choice2=0
                                                        choice1=0
                                                        break
                                                        
                                                    
                                                    
                                                    if choice4==2:
                                                        
                                                        n_price=input("Write the new price for the product : ")
                                                        
                                                        ofile=open('hardware/{}'.format(file_names[n]),"w",newline="")
                                                        writer=csv.writer(ofile)
                                                        
                                                        for row in read_new:
                                                            if row==flist[0]:
                                                                writer.writerow([flist[0][0],flist[0][1],n_price])
                                                                continue
                                                            writer.writerow(row)
                                                        
                                                        ofile.close()
                                                        
                                                        print()
                                                        print("Price has been updated.")
                                                        a=input("Press ENTER to continue: ")
                                                        print()
                                                        
                                                        choice4=0
                                                        choice3=0
                                                        choice2=0
                                                        choice1=0
                                                        break
                                                                                
                                                            
        
update_hardware()
