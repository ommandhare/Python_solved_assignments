"""
get a number from user, write a program to check if number is prime number

"""
num=int(input("enter the number: "))

if(num%1==0 and num%num==0):
    print("number is prime")
else:
    print("number is not prime")