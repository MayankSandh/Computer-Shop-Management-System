class Repairs:
    def __init__(self):
        self.repairs_list = []
    def menu(self):
        print("\033c")
        print("REPAIRS SECTION")
        repair_type = input("\nEnter a brief title to the repair: ")
        repair_cost = int(input("Enter the possible cost of the repair: "))
        self.repairs_list.append([repair_type, repair_cost])
        if input("Do you want to continue? (y/n): ").lower() != "n":
            self.menu()
        else:
            self.name = input("Please fill in your name here: ").strip()
            self.repair_transaction()
    def repair_transaction(self):
        from random import randint
        with open("transactions/List_of_transactions.txt", "a+") as file:
            trlist = [x.rstrip("\n") for x in file.readlines()]
            trno = randint(10000, 99999)
            while trno in trlist:
                trno = randint(10000, 99999)
            file.write(str(trno)+"\n")
        with open("transactions/{}.txt".format(trno), "w") as file:
            file.write('Transaction type: Repairs'+'\n')
            file.write("{:<13s}{:<27d}".format("Transac. No:", trno)+"\n")
            file.write("Name: "+self.name+"\n")
            from datetime import datetime
            dtt = datetime.now().strftime("%a | %d-%m-%Y | %I:%S %p")
            file.write(dtt+"\n")
            file.write("~"*40 + "\n")
            file.write("{:30s}{:10s}".format("REPAIR", "COST") + "\n")
            file.write("~"*40 + "\n")
            amount = 0
            for x in self.repairs_list:
                file.write("{:30s}{:<10d}".format(x[0], x[1]) + "\n")
                amount+=int(x[1])
            file.write("~"*40 + "\n")
            file.write("{:>30s}{:<10d}".format("TOTAL: ", amount) + "\n")
            file.write("~"*40 + "\n")
        print('\nThank you for shopping with us.')
        print(self.name+ ', your unique transaction id is:',trno)
        print("Use option 3 to get your bill.")
        _ = input("\nPress ENTER to exit.")

if __name__ == "__main__":
    m1 = Repairs()
    m1.menu()