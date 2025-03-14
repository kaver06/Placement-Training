#Program to accept name and salary. Check if their salary is >3L and display if they have to pay tax

name=input("Enter your name : ")
salary=int(input("Enter the salary :  "))

if(salary>300000):
    print("Employee", name ,"has to be taxed")
else:
    print("Employee", name ,"should not taxed")