k=int(input())
for i in range(k):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,k):
        print("*",end='')
    print() 

#right sided triangle 