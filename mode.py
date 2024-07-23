from statistics import mode 
def keer(r,c):
    k=r.count(c)
    d=mode(r)
    return k ,d 
r=[5,2,4,8,9,7,5,5,2,5]
c=5 
k,d=keer(r,c)
print(k)
print(d)