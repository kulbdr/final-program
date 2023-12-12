print("WELCOME TO THE GRANN'S PHONE DIRECTORY.\n 1. Add a new record.\n 2. Search a record. \n 3. Update a record. \n 4. Sort the record alphabetically. \n 5. Delete a record. \n 6. Quit")
p=int(input("Enter Your Choice:"))

phoneDirectory={}
while(p!=6):
    if p==1:
        if len(phoneDirectory)>=5:
            print("Cart is full.")
        print("Add a new record.")
        x=input("Enter Name:")
        y=int(input("Enter number:"))
        if len(phoneDirectory)>=5:
            print("Cart is full.")
