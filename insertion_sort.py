def sort(array):
    for i in range(0,len(array)):
        for j in range(i,0,-1):
            if(array[j]<array[j-1]):
                array[j],array[j-1]=array[j-1],array[j]
    return array        

print(sort([1,2,4,3,343,23,44,566,2,23]))            
