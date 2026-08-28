print("Please Enter Employee Name:")
employee_name = input()

print("Please Enter Employee Salary:")
employee_salary = int(input())

print("Please Enter Employee Total Deductions:")
total_deductions = int(input())

total_pay = employee_salary-total_deductions

print(employee_name)
print(total_pay)