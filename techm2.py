def sum1(a,e,p):
    s=0
    for i in range(p-1,a-1):
        s=s+abs(e[i]-e[i+1])
    return s
a=int(input("enter range :;"))
e=list(list(map(int,input("enter the list elemens:;").split())))
p=int(input("enter position:")) 
print(sum1(a,e,p))