k=int(input("enter the range:"))
a=list(map(int,input("enter the array :").split()))
d,f=map(int,input("enter the d,f values :").split()) 
even,odd=0,0
for i in range(k):
    if a[i]%2==0:
        even=even+1 
    else:
        odd=odd+1 
if d%2==0:
    if odd==0:
        print("the fine is by odd vechicle",0)
    else:
        
        print("the  fine collected from odd number vechicle is",f*odd)
else:
    if even==0:
        print(" the fine collected by evn ",0)
    else:
        print("the fine collecte from even vehicle  is ",f*even) 

"""
Particulate matters are the biggest contributors to Delhi pollution. The main reason behind the increase in the concentration of PMs include vehicle emission by applying Odd Even concept for all types of vehicles. The vehicles with the odd last digit in the registration number will be allowed on roads on odd dates and those with even last digit will on even dates.

Given an integer array a[], contains the last digit of the registration number of N vehicles traveling on date D(a positive integer). The task is to calculate the total fine collected by the traffic police department from the vehicles violating the rules.

Note : For violating the rule, vehicles would be fined as X Rs.
"""