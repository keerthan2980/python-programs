k=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in k:
    if i not in a:
        a.append(i)
for i in a:
    if k.count(i)>1:
        b.append(i)
    else:
        c.append(i)
print("are the duplicate",b,a)
print("are not the dublicates",c)