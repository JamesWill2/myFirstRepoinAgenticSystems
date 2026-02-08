marks = [78, 85, 90, 65, 72, 88, 92, 80]

print("First 3 marks:", marks[:3])
print("Last 3 marks:", marks[-3:])

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)