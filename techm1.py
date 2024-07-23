def evenodd(h,ele):
    c=0
    d=0
    for i in ele:
        if i%2==0:
            c=c+1
        else:
            d=d+1 
    return f"the difference between even and odd is{c-d}"
h=int(input("enter the range of  list"))
ele=list(map(int,input().split())) 
print(evenodd(h,ele))