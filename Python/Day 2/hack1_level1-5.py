"""Tax Calculator Problem
GlobalNext Solutions, a rapidly growing IT company, employs a diverse workforce ranging from entrylevel developers to senior executives. The HR department wants to streamline the tax calculation
process for employees under the New Tax Regime (2023). They’ve decided to build a tax calculation
program that computes salaries, taxes, and net incomes while ensuring compliance with the latest tax
laws.
As a software developer in GlobalNext’s HR-Tech team, you are tasked with developing this program.
The system should process employee salary details, validate inputs, calculate taxes, and generate
detailed reports.
Objectives
The program should:
1. Accept employee details, including monthly salary components.
2. Calculate gross and taxable income according to the New Tax Regime (2023).
3. Compute the tax payable using the appropriate tax slabs.
4. Apply any applicable standard deductions and rebates.
5. Generate reports detailing gross salary, taxable income, tax payable, and net salary.
Level 1: Basic Input and Salary Calculation
Objective: Capture employee details and calculate the gross salary.
Tasks:
• Accept the following inputs for an employee:
o Name
o EmpID
o Basic Monthly Salary
o Special Allowances (Monthly)
o Bonus Percentage (Annual Bonus as % of Gross Salary)
• Calculate:
o Gross Monthly Salary = Basic Salary + Special Allowances
o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus
Output:
o Display the employee details, gross monthly salary, and annual gross salary"""

name =input("Enter the name of the Employee : ")
id=input ("Enter the employ ID : ")
sal=float(input("Enter monthly base salary : "))
s_sal=float(input("Enter special allowances : "))
b_per=float(input("Enter bonus percentage : "))
gms=sal+s_sal
b=(b_per*gms)/100
print(b)
ags=(gms*12)+b

"""print("\n \nEmployee Name : ₹",name)
print("Employee ID : ",id)
print("Gross Monthly Salary : ₹",gms)
print(f"Anaual Gross Salary : ₹{ags:.2f}")"""


"""Level 2: Taxable Income Calculation
Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income."""

std_ded_sal=ags-50000

#print(f"Taxable income = {ags} - 50000 = ₹{std_ded_sal:.2f}")

"""Level 3: Tax and Rebate Calculation
Objective: Compute tax payable using the New Tax Regime (2023) slabs.
Tasks:
1. Calculate tax based on the following slabs:
o ₹0- ₹3,00,000: 0%
o ₹3,00,001- ₹6,00,000: 5%
o ₹6,00,001- ₹9,00,000: 10%
o ₹9,00,001- ₹12,00,000: 15%
o ₹12,00,001- ₹15,00,000: 20%
o Above ₹15,00,000: 30%
2. Apply Section 87A Rebate:
o Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0).
3. Add a 4% Health and Education Cess to the calculated tax.
Output:
• Display a detailed tax breakdown, including slabs, cess, and total tax payable."""


tax_amt=0
if(std_ded_sal<300000):
    tax_amt= 0
    #print("₹0- ₹3,00,000: 0% Tax applicalbe")
elif(std_ded_sal<600000 and std_ded_sal>300001):
    tax_amt=(5/100)*std_ded_sal
    #print("₹3,00,001- ₹6,00,000: 5% Tax applicalbe")
elif(std_ded_sal<900000 and std_ded_sal>600001):
    tax_amt=(10/100)*std_ded_sal
    #print("₹6,00,001- ₹9,00,000: 10% Tax applicalbe")
elif(std_ded_sal<1200000 and std_ded_sal>900001):
    tax_amt=(15/100)*std_ded_sal
    #print("₹9,00,001- ₹12,00,000: 15% Tax applicalbe")
elif(std_ded_sal<1500000 and std_ded_sal>1200001):
    tax_amt=(20/100)*std_ded_sal
    #print("₹12,00,001- ₹15,00,000: 20% Tax applicalbe")
elif(std_ded_sal>1500000):
    tax_amt=(30/100)*std_ded_sal
if(std_ded_sal<70000):
    new_taxamt=0
"""    print("Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0)")
print("Total tax amount: ",tax_amt)
print("Health and educational cess = 4%")"""
new_taxamt=(4/100)*tax_amt+tax_amt


"""Level 4: Net Salary Calculation
Objective: Calculate annual net salary after tax deductions.
Tasks:
1. Compute Net Salary = Annual Gross Salary- Total Tax Payable.
2. Display:
o Annual Gross Salary
o Total Tax Payable (including cess)
o Annual Net Salary"""

net_sal=std_ded_sal-new_taxamt
"""print(f"Anaual Gross Salary : ₹{ags:.2f}")
print("Final tax amount including cess is ",new_taxamt)
print("Annual Net Salary : ",net_sal)"""


print("\n \nEmployee Name    :                ",name)
print("Employee ID :                     ",id)
print("Gross Monthly Salary : ₹          ",gms)
print(f"Anaual Gross Salary :             ₹{ags:.2f}")
print(f"Taxable income =                  ₹{std_ded_sal:.2f}")
print("Total tax amount:                 ",tax_amt)
print("Health and educational cess =      4%")
print("Final tax amount including cess is:",new_taxamt)
print("Annual Net Salary :               ",net_sal)














