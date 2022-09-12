#Write a program to reverse a stack.

class Stack(object):
    def __init__(self):
        self.item=[]

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if self.item==[]:
            return None
        else:
            return self.item.pop()

    def size(self):
        return len(self.item)


    def isempty(self):
        return self.item==[]

def reverse(str):
    TemStr=" "
    stack=Stack()

    for i in range(len(str)):
        stack.push(str[i])

    while not stack.isempty():
        Tem=stack.pop()
        TemStr= TemStr + Tem
    return TemStr

if __name__=="__main__":
    print(reverse("Chandan Bauri"))