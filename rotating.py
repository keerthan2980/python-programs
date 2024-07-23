def rotat(arr,k):
    n=len(arr)
    k=k%n
    return arr[-k:]+arr[:-k]
arr= list(map(int,input("enter the arr elements ").split()))
k=int(input("enter the k values ")) 
print("the result is",rotat(arr,k))