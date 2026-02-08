balance = int(input("Enter balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
verified_input = input("Verified (True/False): ")

verified = verified_input.lower() == "true"

if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")