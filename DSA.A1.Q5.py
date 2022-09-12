#Read about the Tower of Hanoi algorithm. Write a program to implement it.

def hanoi(n,A,C,B):
    if n==0:
        return
    hanoi(n-1,A,B,C)
    print("Shift disk", n, "from",A, "to", C)
    hanoi(n-1,B,C,A)
n=3
hanoi(n, "A", "B", "C")