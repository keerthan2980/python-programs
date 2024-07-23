#multiple of all elements in list 
def a(l):
    r=1
    for i in l:
        r=r*i 
    return r 
l=list(map(int,input().split()))
print("the answers is ",a(l))