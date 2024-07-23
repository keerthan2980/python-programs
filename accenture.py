a=int(input())
a=str(a)
k=a 
if a[::-1]=="0":
    k=a[0:len(a)-1]
print(k[::-1])
