contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("✅ Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} - {c['phone']}")
    print()

def search_contact():
    keyword = input("Search by name or phone: ").lower()
    found = False
    for c in contacts:
        if keyword in c['name'].lower() or keyword in c['phone']:
            print("\n🔍 Contact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}\n")
            found = True
            break
    if not found:
        print("❌ Contact not found.\n")

def update_contact():
    name = input("Enter name of contact to update: ").lower()
    for c in contacts:
        if name == c['name'].lower():
            print("Enter new details (leave blank to keep current):")
            new_name = input(f"Name [{c['name']}]: ") or c['name']
            new_phone = input(f"Phone [{c['phone']}]: ") or c['phone']
            new_email = input(f"Email [{c['email']}]: ") or c['email']
            new_address = input(f"Address [{c['address']}]: ") or c['address']

            c.update({'name': new_name, 'phone': new_phone, 'email': new_email, 'address': new_address})
            print("✅ Contact updated!\n")
            return
    print("❌ Contact not found.\n")

def delete_contact():
    name = input("Enter name of contact to delete: ").lower()
    for c in contacts:
        if name == c['name'].lower():
            contacts.remove(c)
            print("🗑️ Contact deleted!\n")
            return
    print("❌ Contact not found.\n")

def menu():
    while True:
        print("📱 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        print()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting Contact Book.")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

menu()
