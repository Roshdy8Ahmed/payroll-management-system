def calculate_bonus(base_salary , rating):
    if rating == 5 :
        return base_salary*0.2
    elif rating == 4 or rating == 3 :
        return base_salary*0.1
    else:
        return 0.0 

def calculate_tax(gross_salary):
    if gross_salary > 7000 :
        return gross_salary * 0.15
    elif gross_salary >= 3000 :
        return gross_salary * 0.1
    else:
        return 0.0

def main_hr_app():
     print("--- Corporate Payroll System ---")
     employee_name = input("Enter Employee Name: ")
     base_salary = float(input("Enter Base Salary (EGP): "))
     rating = int(input("Enter Performance Rating (1-5): "))

     if rating < 1 or rating > 5 or base_salary < 0:
         print(" Invalid data entered. Please restart and check your inputs.")
         return
     bonus = calculate_bonus(base_salary, rating)
     gross_salary = base_salary + bonus
     tax = calculate_tax(gross_salary)
     net_salary = gross_salary - tax
     
     print("\n" + "+" + "-"*38 + "+")
     print(f"|  PAYROLL STATEMENT: {employee_name:<15} |")
     print("+" + "-"*38 + "+")
     print(f"| Base Salary     : {base_salary:>10.2f} EGP |")
     print(f"| Earned Bonus    : {bonus:>10.2f} EGP |")
     print(f"| Tax Deductions  : {tax:>10.2f} EGP |")
     print("+" + "-"*38 + "+")
     print(f"| NET PAYABLE     : {net_salary:>10.2f} EGP |")
     print("+" + "-"*38 + "+")
main_hr_app()






