"""
get a number from user, write a program to check if number is prime number

"""
num=int(input("enter the number: "))
flag=0
if(num==1):
    print("number is prime")
elif(num>1):
    for i in range(2,num):
         if num%i==0 :
            print("ddd")
            flag=1
            break


if flag==1:
    print(" number is not prime")
else:
    print(" number is prime")