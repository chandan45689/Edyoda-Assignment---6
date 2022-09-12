#Write a program to print the first non-repeated character from the string.

def isrepeated(w1):
    w3=""
    for i in w1:
        if i not in w3:
            w3=w3+i
    print(w3)
a="Chandan"
isrepeated(a)



