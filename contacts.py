contacts = {}

while True:
    print("=============== Contacts App ===============")
    print("1. Add Contacts")
    print("2. Search Contacts")
    print("3. Delete Contacts")
    print("4. Update Contacts")
    print("5. View All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        mob_no =int(input("Enter new mobile no : "))

        if mob_no in contacts:
            print("Already Exists....")
        else:
            name =input("Enter name : ")
            contacts[mob_no] = name
            print("Contact Added Successfully....")
    
    elif choice == 2:
        mob_no =int(input("Enter mobile number : "))

        if mob_no in contacts:
            print(mob_no,contacts[mob_no])
        else:
            print("Contact not found....")

    elif choice == 3:
        mob_no =int(input("Enter mobile number : "))

        if mob_no in contacts:
            contacts.pop(mob_no)
            print("Contact Delete Successfully....")
        else:
            print("Contact not found....")

    
    elif choice == 4:
        mob_no =int(input("Enter mobile no : "))

        if mob_no in contacts:
            name =input("Enter Updated name : ")
            contacts.update({mob_no : name})
            print("Contact Update Successfully....")
        else:
            print("Contact not found....")

    elif choice == 5:

        if len(contacts) == 0:
            print("No Contacts....")
        else:
            print("Mob No :  Name")
            for i in contacts:
                print(i,"\t",  contacts[i])
    elif choice == 6:
        print("Thank You....")
        break

    else:
        print("Invalid Choice...\nEnter Again...")
