k=int(input())
c=0
for i in range(1,k+1):
    if k%i==0:
        c=c+1
if c==2:
    print("prime")
else:
    print("not")
