def subarray(arr,k):
    n=len(arr)
    if k>n:
        return None 
    sub=[]
    minm=[]
    for i in range(n-k+1):
        sub1=arr[i:i+k]
        sub.append(sub1)
        print(sub)
        min_v=min(sub1)
        minm.append(min_v)
        print(minm)
    return max(minm)

k = int(input("Enter the subarray length: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
print(subarray(arr, k))
