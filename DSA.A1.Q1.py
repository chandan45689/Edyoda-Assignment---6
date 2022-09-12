#Write a program to find all pairs of an integer array whose sum is equal to a given number.

def function(list,output,n):
    for i in range(n):
        for j in range(i+1):
            if array[i] + array[j] == given_result:
                print(array[i], array[j])

array=[1,2,3,4,5,6,7,8]
given_result=9

function(array,given_result,len(array))