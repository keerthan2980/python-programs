k=int(input())
j=0
L=[0 for i in range(k)]
#program for getting all the zeros last of the array without changeing the order of the actual array it was tcs question 2024
for i in range(k):
    a=int(input())
    if a!=0:
        L[j]=a
        j=j+1
for i in L:
    print(i,end=" ")