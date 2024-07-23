k=int(input())
for i in range(k):
    print(" "*(k-i),end=" ")
    for j in range(i+1):
        print("*",end=' ')
    print() 

"""
for reverse 
n = 5
for i in range( n):
    print(" " * (i), end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
"""