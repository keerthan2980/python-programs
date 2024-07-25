k=int(input())
l=[]
for i in range(k):
    l.append(int(input()))
print(l)
c=0
a=[]
for e in set(l):
    if l.count(e)>1:
        a.append(e)
        c=c+l.count(e)-1
        print(c)
print(a,c)
#it will print the count of element -1 