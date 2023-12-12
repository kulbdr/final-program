print("WELCOME TO THE GRANN'S PHONE DIRECTORY.\n 1. Add a new record.\n 2. Search a record. \n 3. Update a record. \n 4. Sort the record alphabetically. \n 5. Delete a record. \n 6. Quit")
p=int(input("Enter Your Choice:"))

phoneDirectory={}

while(p!=6):
    if p==1:
        print("Add a new record.")
        x=input("Enter Name:")
        y=int(input("Enter your 10 digit phone number:"))
        phoneDirectory.update({x:y})
        print("Record Added.")
        print(phoneDirectory)
       
    elif p==2:
        search=input("2. Search for a product:")
        if search in phoneDirectory:
            print(search,":",phoneDirectory[search])
        else:
            print("Record not found.")

    elif p==3:
        u=input("Update a record:")
        if u in phoneDirectory:
            newnumber=int(input("Enter new 10 digit number."))
            phoneDirectory.update({u:newnumber})
            print("New record updated")
            print(phoneDirectory)
        else:
            print("Record not found.")

    elif p==4:
        sort=sorted(phoneDirectory.items())
        print("Sorted Record is:",sort)

    elif p==5:
        d=input("Enter record you want to delete:")
        if  d in phoneDirectory:
            phoneDirectory.pop(d)
            print("Record Delete")
        else:
            print("Record not found")

    elif p==6:
        print("Quit")
    
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY.\n 1. Add a new record.\n 2. Search a record. \n 3. Update a record. \n 4. Sort the record alphabetically. \n 5. Delete a record. \n 6. Quit")
    p=int(input("Enter Your Choice:"))



    

        
