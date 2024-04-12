path = r"C:\Users\HP\Desktop\Philomath\python_codes\.venv\Assignments\users.csv"

count=0
users = []
for line in open(path):
    if(count==0):
        count +=1
        continue
    print(line,end="")
    user,password= line.strip().split(",")
    users.append((user,password))

while(1):
    ch=input("enter q to exit/any key continue ")
    if(ch=="q"):
        break
    else:
        entereduser=input("enter name to search : ")
        entereduser=str(entereduser)
        for i in user:

            print(entereduser + " is valid user")
        else:
            print(entereduser + " is not valid user ")
