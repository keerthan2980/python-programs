def fmiss(gl):
    n=len(gl)+1 
    asum=sum(gl)
    tsum=n*(n+1)//2 
    return tsum-asum 
gl=list(map(int,input().split()))
print("the missing number is",fmiss(gl))