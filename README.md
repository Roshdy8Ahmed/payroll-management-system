# payroll-management-system
A modular Python console application that simulates a corporate HR and payroll backend — calculating employee bonuses and tax deductions based on performance ratings and salary brackets.
## Features
- Calculates performance-based bonuses (0%, 10%, or 20%)
- Calculates progressive tax deductions based on salary brackets
- Validates user input (salary and rating ranges)
- Displays a formatted payroll summary
## Installation
1. Make sure Python 3 is installed on your machine.
2. Clone this repository:
3. 
4. Run the program:
```
   python main.py
```
## Example Run
```
--- Corporate Payroll System ---
Enter Employee Name: Roshdy
Enter Base Salary (EGP): 8000
Enter Performance Rating (1-5): 5

+--------------------------------------+
|  PAYROLL STATEMENT: Roshdy             |
+--------------------------------------+
| Base Salary     :    8000.00 EGP |
| Earned Bonus    :    1600.00 EGP |
| Tax Deductions  :    1440.00 EGP |
+--------------------------------------+
| NET PAYABLE     :    8160.00 EGP |
+--------------------------------------+
```
