import pandas as pd
import numpy as np

#sample dataset
data = {
    "Employee": [
        "Sneha", "Vikram", "Arjun", "Kartik",
        "Ansh", "Priya", "Anjali", "Divya"
    ],
    
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    
    "Temporary_Notes": [
        "On probation", "Contract", "Pending docs", "Verified",
        "Intern", "New joiner", "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

#Detect missing values
print("\nMissing Values:")
print(df.isnull().sum())

#Fill missing Salary values with column mean
mean_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(mean_salary)

print("\nAfter Filling Missing Salary with Mean:")
print(df)

#Drop Temporary Notes column
df = df.drop(columns=["Temporary_Notes"])

print("\nAfter Dropping Temporary_Notes Column:")
print(df)

#Rename Salary → Annual_Salary
df = df.rename(columns={"Salary": "Annual_Salary"})

print("\nAfter Renaming Column:")
print(df)

#Group by dept
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

#final summary
print("\nDepartment Summary:")
print(summary)