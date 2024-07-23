k=int(input())
a,b=0,1
print("fs",a ,b,end=" ")
for i in range(2,k):
    c=a+b
    a=b
    b=c
    print(c,end=" ")