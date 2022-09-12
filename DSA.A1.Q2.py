#Write a program to reverse an aray in place? In place means you cannot create a new array. You have to update the original arrayl

def reverse(array,n):
    i=0
    j=n-1
    while i < j:
        array[i],array[j]=array[j],array[i]
        i=i+1
        j=j-1
    print(array)
list=[1,2,3,4,5,6,7,8,9]
reverse(list,len(list))