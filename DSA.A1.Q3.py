#Write a program to check if two strings are rotation of each other or not.

def isrotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        s3=s1+s1
        if s2 in s3:
            return True
        else:
            return False

a="Its Raining Today"
b=" Raining TodayIts"

print(isrotation(a,b))


