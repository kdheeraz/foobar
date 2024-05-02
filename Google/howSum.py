def howSum(target,arr,memo={}):
    if(memo.get(target)):
        return memo.get(target)
    if(target==0): return []
    if(target<0): return None
    for ele in arr:
        remainder_pos = howSum(target-ele,arr)
        if remainder_pos !=None:
            memo[target]=[]+remainder_pos+[ele]
            return []+remainder_pos+[ele]
    memo[target]=None
    return None    


print(howSum(1000,[3,5,7]))