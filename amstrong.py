k=int(input())
s=k 
b=len(str(k))
h=0
while k!=0:
    a=k%10 #reminder
    h=h+(a**b)
    k=k//10 #quoitent 
if h==s:
    print("amstrong")
else:
    print("not")