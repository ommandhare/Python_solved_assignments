"""
read the testDuplicate file and find duplicate lines in file

"""


path=r"C:\Users\HP\Desktop\Philomath\python_codes\.venv\Assignments\duplicate.txt"
lineList=[]
duplicateList=[]
for line in open(path):
    print(line)

for line in open(path):
    line=line.strip().split(",")

    if(line in lineList):
        duplicateList.append(line)
    else:
        lineList.append(line)

print("line List")
print(lineList)
print("duplicate List   ")
print(duplicateList)




