#sum factors of the number is equal to the number then it is called perfect
k=int(input("enter the number for checking perfect or not:"))
s=[]
for i in range(1,k):
    if k%i==0:
        s.append(i)
print("list of factors",s,"if strong print",sum(s)==k)