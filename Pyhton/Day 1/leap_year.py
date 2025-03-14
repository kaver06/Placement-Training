#Program to check if a year given is a leap year or not

year=int(input("Enter the year : "))
p=year//4==0
print(p)
if(year%4==0):
    print("It s a leap year")
else:
    print("Its not a leap year ")