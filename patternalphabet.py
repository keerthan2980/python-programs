k=int(input())
av=65
for i in range(k):
    for j in range(i+1):
        a=chr(av)
        print(a,end=" ")
    av=av+1 
    print()