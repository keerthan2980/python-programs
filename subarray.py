k=3 #length of sub array 
h=[1,2,3,1,2] #array 
sub=[]
l=len(h)
for i in range(l-k+1):
    subarray=h[i:i+k]
    sub.append(subarray)
print(sub)


def subarray(h,k):
    l=len(h)
    sub=[]
    for i in range(l-k+1):
        subarray=h[i:i+k]
        sub.append(subarray)
    return sub 
k=int(input("enter the sub array length"))
h=list(map(int,input().split()))
print(subarray(h,k))