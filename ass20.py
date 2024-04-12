"""
get a character from user and check if the character is number or vovel or conconent

"""

str=input("enter the character: ")
vowelList=["a","e","i","o","u"]
numList=["0","1","2","3","4","5","6","7","8","9"]
if str in vowelList :
    print("character is vowel")
elif str in numList:
    print("character is number")
else:
    print("character is consonent")