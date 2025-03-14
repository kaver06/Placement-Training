
arr=[]
for i in range(5):
    arr.append(int(input("No : ")))

arr.sort()
arr=list(set(arr))
print(f"Second largest :{arr[len(arr)-2]}\nSecond Smallest {arr[2]}")
print(arr)





"""for p in range(arr):
    if(arr[i]>arr[i-1]):
        num=arr[i]
    else:
        num=num
print("First biggest is ",num)
second_num=0
for q in range (arr):
    if(arr[i]<num and arr[i]>arr[i-1]):
        second_num=arr[i]
    else:
        second_num=second_num
print("second biggest is ",second_num)

"""
