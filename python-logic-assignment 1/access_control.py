age = int(input("Enter age: "))
has_id_input = input("Do you have an ID (True/False): ")

has_id = has_id_input.lower() == "true"

if age >= 18 and has_id:
    print("Entry allowed")