def howSum(target,arr,memo={}):
    if(memo.get(target)):
        return memo.get(target)
    if(target==0): return []
    if(target<0): return None
    minLs=[]
    for ele in arr:
        remainder_pos = howSum(target-ele,arr)
        if remainder_pos !=None:
            if(len(minLs)==0):
                minLs=[]+remainder_pos+[ele]
            elif(len(minLs)>len([]+remainder_pos+[ele])):
                minLs=[]+remainder_pos+[ele]
    memo[target]=minLs            
    return minLs
   


print(howSum(1000,[2,3,5,7]))