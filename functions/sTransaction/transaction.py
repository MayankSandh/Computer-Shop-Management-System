import csv
from random import randint
class Transaction:
    def __init__(self):
        # initialising the product and item-ordered list
        self.products = ["antivirus", "cloud storage", "games"] 
        # !! The names in the self.products list much match with the CSV FILENAMES in the software folder
        self.items_ordered = [] # this list will save the duplets of (item_name, price) 
        #                           and you can use this data later eg. for cash_memo
        # this function must be used to mantain the transaction list
    
    def menu0(self): # The PRODUCT CATEGORIES menu
        print("\033c")# clear-screen character
        print(50*"~")
        print("PRODUCT CATEGORIES")
        print(50*"~")
        print('0) Enter 0 to exit.')
        sno = 1
        for p in self.products: # listing out the names of CATEGORIES along with the option no.
            print(str(sno)+")", p.title())
            sno+=1
        print(50*"~")
        print()
        # self.choice is the choice of the menu0
        self.choice = int(input("Choose which option: "))
        if self.choice == 0: # zero is a special input which will do some other func
            # example here: cash memo
            # use this condition statement to maintain the transaction
            if self.items_ordered == []:
                if input("You have no items in your cart. Are you sure you want to exit?(y/n): ").lower()=='y':    
                    import main_menu
                    main_menu()
                else:
                    self.menu0()
            else:
                print("You have",len(self.items_ordered),'item in your cart.')
                if input('Do you wish to continue your purchases(y/n): ').lower()=='n':
                    name = input("Enter your name here: ")
                    with open("transactions/List_of_transactions.txt", "a+") as file:
                        trlist = [x.rstrip("\n") for x in file.readlines()]
                        trno = randint(10000, 99999)
                        while trno in trlist:
                            trno = randint(10000, 99999)
                        file.write(str(trno)+"\n")
                    t = trno
                    with open("transactions/{}.txt".format(t), "w") as file:
                        file.write('Transaction type: Software'+'\n')
                        file.write("{:<13s}{:5d}".format("Transac. No:", t)+"\n")
                        file.write("Name: "+name+'\n')
                        from datetime import datetime
                        dtt = datetime.now().strftime("%a | %d-%m-%Y | %I:%S %p") 
                        file.write(dtt+"\n")
                        file.write("-"*120 + "\n")
                        file.write("{:100s}{:10s}".format("ITEMS ORDERED BY:"+' '+name, "COST") + "\n")
                        file.write("-"*120 + "\n")
                        amount = 0
                        for x in self.items_ordered:
                            file.write("{:<100s}{:<10d}".format(x[0], x[1]) + "\n")
                            file.write('\n')
                            amount+=int(x[1])
                            
                        file.write("-"*120 + "\n")    
                        file.write("{:<100s}{:<10d}".format("TOTAL: ", amount) + "\n")
                        file.write("-"*120 + "\n")
                    print('\nThank you for shopping with us.')
                    print(name+ ', your unique transaction id is:',t)
                    print("Use option 3 to get your bill.")
                    _ = input("\nPress ENTER to exit.")
                else:
                    self.menu0()
        else:
            self.menu1()
    def menu1(self): # this is the first sub-menu (menu1) under PRODUCT CATEGORIES
        print("\033c")
        print(50*"~")
        # The following is the header of the function which shows us we are in which option
        print("PRODUCT CATEGORIES >>", self.products[self.choice-1].title())
        print(50*"~")
        # we are accessing the csv file inside software folder with the name/category chosen in menu0
        with open("software/{}.csv".format(self.products[self.choice-1])) as file:
            self.categories = [] # this category is the list of company names
            # not to be confused with the PRODUCT CATEGORIES in menu0
            self.sub = dict() # sub key is the dictionary which will have COMPANY as the key
            #                   and the duplets of (item_name, price) as its values
            i = 1
            for p in csv.reader(file):
                if p[0] not in self.categories:
                    self.categories.append(p[0]) # storing all the company names in self.categories
                    print(str(i)+")",p[0])
                    i+=1
                if p[0] not in self.sub.keys(): # this loop is initialising (accessing first time)
                    #                            the key(company) for the dict
                    self.sub[p[0]] = list() # making a container to store the duplets for the key
                    self.sub[p[0]].append([p[1], p[2]])
                else: # is the company name is already available in the dict, store the duplet
                    self.sub[p[0]].append([p[1], p[2]])
            print(50*"~")
            print()
        self.choice2 = int(input("Choose which option2: ")) # choosing the second option (company) which the user wants
        if self.choice2 == 0: # 0 is the special character which allows the user to move back in the menus
            self.menu0()
        else: # go forward to the second sub-sub-menu (menu2)
            self.menu2()
    def menu2(self):
        print("\033c")
        print(50*"~")
        print("PRODUCT CATEGORIES >>", self.products[self.choice-1].title(), ">>", self.categories[self.choice2-1])
        print(50*"~")
        i = 1 # options
        for item in self.sub[self.categories[self.choice2-1]]: # iterating all the duplets and printing
            print(str(i)+")", item[0]) # printing the item name from the duplet
            print("\t\t\tPrice:",item[1]) # printing the price in the duplet
            i+=1
        print(50*"~")
        print()
        self.choice3 = int(input("Which one do you choose to buy?: ")) # chosing which product to buy in menu2
        if self.choice3 == 0: # goes back to menu1
            self.menu1()
        else:
            self.items_ordered.append([item[0], int(item[1])]) # add this item to the items_ordered section
            print("SUCCESSFULLY ADDED TO CART!")
            if input("Do you want to go back? (y/n):").lower() == "y":
                self.menu0()
            else:
                self.menu2()

if __name__ == "__main__":
    m1 = Transaction()
    m1.menu0()
