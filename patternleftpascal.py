k=int(input())
for i in range(k):
    for j in range(i+1):
        print("*",end="") 
    print()
for i in range(k-1):
    for j in range(i,k-1):
        print("*",end='')
    print() 