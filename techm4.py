def evenodd(k,ele):
    c=[]
    d=[]
    for i in range(len(ele)):
        if i%2==0:
            c.append(ele[i])
        else:
            d.append(ele[i])
    return c,d,(sum(c)-sum(d))
k=int(input("enter the range"))
ele=list(map(int,input().split()))
print(evenodd(k,ele))