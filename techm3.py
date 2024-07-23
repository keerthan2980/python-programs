k=int(input("enter the range "))
ele=list(map(int,input("enter the elements").split()))
r=[]
for i in ele:
    h=i//12
    r.append(h)
k=sum(r)
print(f"sum is {r,k}")