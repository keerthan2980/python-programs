k=input("enter the value of k")
a=k[::-1]
if k==a:
    print("yes")
else:
    print("no") 

def pal(r):
    b=r[::-1]
    if b==r:
        print("yes")
    else:
        print("no")
r=input()
pal(r)