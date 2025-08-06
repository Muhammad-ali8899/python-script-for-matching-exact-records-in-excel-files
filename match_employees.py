import pandas as pd

# Load both Excel files
Emp_df = pd.read_excel("d:/Data Analytics/Emp.xlsx")
PerformanceR_df = pd.read_excel("d:/Data Analytics/PerformanceR.xlsx")

# Make sure the column name is exactly the same in both
# For example: 'Employee_Number'
# You can rename columns if needed
# nadra_df.rename(columns={'EmpNo': 'Employee_Number'}, inplace=True)

# Merge datasets on Employee Number (inner join gives matched records)
matched_df = pd.merge(Emp_df, PerformanceR_df, on='EmployeeID', how='inner')

# Save matched records to new Excel file
matched_df.to_excel("d:/Data Analytics/matched_employees_Emp_Per.xlsx", index=False)

print(f"Total matched records: {len(matched_df)}")
