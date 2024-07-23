#strong number means sum of factorial of each digit of the orginal number
orginal=int(input("enter the strong number to check::"))
n=orginal
li=[]
li2=[]
while n>0:
    r=n%10
    li.append(r)
    n=n//10 
print("this are the digits of orginal number::",li)
#function for factorial
def fn(num):
    if num==0 or num==1:
        return 1 
    else:
        return num*fn(num-1)
for i in li:
    lit=fn(i)
    li2.append(lit)
print("this are the factoria of each digit orginal number::",li2)
# the sum elements in a list can be writen in sumfod = sum(fn(ele) for ele in h)
sumli=sum(li2)
print("sum of the factorial::",sumli)
#print(n)
#print(orginal)
#comparing with the orginal
if orginal==sumli:
    print("It is a strong number") 
else:
    print("It is a not a strong number")