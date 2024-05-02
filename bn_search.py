def binary_search(st,end,arr,ele):

    mid = int((st+end)/2)
    
    if(st>end):
        return st
    if(mid==0):
        return -1
    if(ele==arr[mid]):
        return mid
    elif(ele<arr[mid]):
        return binary_search(st,mid-1,arr,ele)
    elif(ele>mid):
        return binary_search(mid+1,end,arr,ele)
    return mid       
    
a=[1,2,5,6,88,212,234]
print(binary_search(0,len(a)-1,a,11))    