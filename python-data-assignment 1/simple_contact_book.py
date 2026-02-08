contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Suresh": "9988776655"
}

print("All contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)

search_name = input("Enter name to search: ")

if search_name in contacts:
    print("Phone number:", contacts[search_name])
else:
    print("Contact not found")