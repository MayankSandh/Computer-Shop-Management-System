def main_menu(): 
    print("\033c") # This is the clear-screen character and it will clear the terminal.
    print("╔"+48*"═"+"╗")
    print("║{:^48s}║".format("╔═──────────────────────────────═╗"))
    print("║"+"│  WELCOME TO TMS INFOSOLUTIONS  │".center(48, "░")+"║")
    print("║{:^48s}║".format("╚═──────────────────────────────═╝"))
    print("║{:^48s}║".format(" [ MAIN MENU ] "))
    print("║  {:46s}║".format(""))
    print("║  {:46s}║".format("1.  Customer Transaction (Hardware)"))   # COMPLETED & DEBUGGED
    print("║  {:46s}║".format("2.  Customer Transaction (Software)"))   # COMPLETED & DEBUGGED
    print("║  {:46s}║".format("3.  Cash Memo")) # COMPLETED & DEBUGGED
    print("║  {:46s}║".format("4.  Transaction History of Date")) # COMPLETED & DEBUGGED
    print("║  {:46s}║".format("5.  Transaction History of Customer")) # COMPLETED & DEBUGGED
    print("║  {:46s}║".format("6.  Updating the Hardware List"))    ### COMPLETED BUT NOT DEBUGGED 
    print("║  {:46s}║".format("7.  Updating the Software List"))    ### COMPLETED BUT NOT DEBUGGED
    print("║  {:46s}║".format("8.  Repair Works"))  # COMPLETED & DEBUGGED
    print("║  {:46s}║".format("9.  List of Workers"))   # COMPLETED & DEBUGGED
    print("║  {:46s}║".format("10. Hire/Fire Workers"))     # COMPLETED  
    # print("║  {:46s}║".format("11. Stocks Tally"))
    print("║  {:46s}║".format("11. Quit"))  # COMPLETED & DEBUGGED
    print("║  {:46s}║".format(""))
    print("╚"+48*"═"+"╝")
    while True:
        choice = (input("Enter your choice (1-11): "))
        if choice not in [str(x) for x in range(1, 13)]:
            print("Please enter a valid choice! ()")
        else:
            choice = int(choice)
            break
    print(50*" ")
    if choice == 11:
        from functions.Quit import QuitMsg
        QuitMsg.quit()
    elif choice == 1: # Use this as the option choser
        # import the required function here when pressed 1
        # example: from functions.package1 import func1
        from functions.hTransaction import transaction
        m1 = transaction.Transaction()
        m1.menu0()
        main_menu()
    elif choice == 2:
        from functions.sTransaction import transaction
        m1 = transaction.Transaction()
        m1.menu0()
        main_menu()
    elif choice == 3:
        from functions.Cashmemo import cash_memo
        cash_memo.cash_memo()
        main_menu()
    elif choice == 4:
        from functions.Transaction_history import transaction_by_date
        transaction_by_date.transaction_by_date()
        main_menu()
    elif choice == 5:
        from functions.Transaction_history import transaction_by_name
        transaction_by_name.transaction_by_name()    
        main_menu()
    elif choice == 6:
        from hardware.update_hardware import update_hardware
        update_hardware()
        main_menu()
    elif choice == 7:
        from software.update_software import update_software
        update_software()
        main_menu()
    elif choice == 8:
        from functions.Repairs import repairs
        m1 = repairs.Repairs()
        m1.menu()
        main_menu()
    elif choice == 9:
        from functions.option910 import workerlist
        workerlist.workerlist()
        main_menu()
    elif choice == 10:
        from functions.option910 import workerlist
        workerlist.hirefireworkers()
        main_menu()
main_menu()
