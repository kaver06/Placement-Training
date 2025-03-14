#To find the largest of 3 numbers

a=int(input("enter the first digita : "))
b=int(input("Enter the second digit : "))
c=int(input("Enter the third digit : "))

if(a>b):
    if(a>c):
        print(a , "is greater")
    else:
        print(c , "is greater")
elif(b>c):
    print(b , "is greater")
else:
        print(c , "is greater")
