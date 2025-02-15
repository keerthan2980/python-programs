k=789456
r=0

while k>0:
    d=k%10 
    r=r*10+d 
    k=k//10
print(r) 



k=[1,6,2,9,8,3]
n=len(k)
for i in range(n):
    for j in range(0,n-i-1):
        if k[j]>k[j+1]:# for accending order
        #if k[j]<k[j+1]:# for decending order order
            k[j],k[j+1]=k[j+1],k[j]
print(k)

k=[1,25,9,7,5,6,78,9]
count=0
for ele in k:
    count=count+1 
print(count)
for i in range(count):
    for j in range(0,count-i-1):
        if k[j]>k[j+1]:
            k[j],k[j+1]=k[j],k[j+1]
print(k)