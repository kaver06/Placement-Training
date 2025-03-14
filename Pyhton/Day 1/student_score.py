''''Write a program to accept a student’s name and scores in three subjects. Display the total, average,
and class secured based on the following criteria:
• 1st Class: Average score of 60 and above.
• 2nd Class: Average score of 50 and above.
• Pass Class: Average score of 35 and above.
• Fail: Average score less than 35.'''

name=input("Enter the name of the student : ")
sub1=int(input("Enter the subject 1 marks : "))
sub2=int(input("Enter the subject 2 marks : "))
sub3=int(input("Enter the subject 3 marks : "))

total=sub1+sub2+sub3
ave=(sub1+sub2+sub3)/3

print("Total = ",total)
print("Average score = ",float(ave))

if(ave>=60):
    print("Result = First class")
elif(ave>=50):
    print("Result = Second class")
elif(ave>=35):
    print("Result = Pass")
elif(ave<35):
    print("Failed")






