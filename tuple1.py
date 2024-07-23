a=[1,2,3,6,"hello",[5,"cs",45]]
"""
f,g,c,h=a we should assign every element in the tuple other wise we will get error 
print(f,g,c,h) 

l1=[1,2,3]
l2=[4,5,6]
for k in zip(l1,l2):
    print(k)

k=enumerate(a)
h=list(enumerate(a)) 
print(k,h)
for index,value in enumerate(a):
    print(index) 
 
i1,*i2=a #from 2nd item in the tuple it will print
print(i2) 
""" 
print(a[5]:1)