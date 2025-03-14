num=int(input("Enter a number : "))
sum=0
while num>0:
    sum += int(num%10)
    num /= 10
print(sum)

"""for i in str(num):
    sum+=int(i)
print("Sum of digits of no is ",sum)"""