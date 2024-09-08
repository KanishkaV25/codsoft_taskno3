contact = {}

def display_contact():
    print("Name\tContact Number\t\tEmail\t\tAddress")
    for key in contact:
        print("{}\t\t{}\t\t{}\t\t{}".format(key , contact[key][0], contact[key][1], contact[key][2]))
    
while True:
     choice = int(input("1. Add Contact\n2. Display Contact\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\nEnter your choice:"))
     if choice==1:
        name = input("Enter the name:")
        phone = input("Enter the Mobile Number:")
        email = input("Enter your email:")
        address = input("Enter your address:")
        print("Contact Saved!!")

        contact[name] = [phone, email , address]

     elif choice==2:
        if not contact:
            print("Not in the Contacts")
        else:
            display_contact()

     elif choice ==3:
            search_name = input("Enter the Contact name you want to search:")
            if search_name in contact:
                print(search_name," contact details is",contact[search_name])
            else:
                print("Name not found in contact book")

     elif choice == 4:
            update_contact = input("Enter contact you want to edit:")
            if update_contact in contact:
                phone = input("Enter Mobile Number:")
                address = input("Enter the new address:")
                email = input("Enter the email:")
                contact[update_contact]=[phone , email, address]
                print("Contact updated!!")
                display_contact()
            

     elif choice ==5:
            del_contact = input("Enter the contact you want to delete:")
            if del_contact in contact:
                confirm = input("Do you want to delete this contact y/n ?")
                if confirm =="y" or confirm =="Y":
                    contact.pop(del_contact)
                    display_contact()
                else:

                    print("Name not found in Contact book")
         
        
     else:
        break


    