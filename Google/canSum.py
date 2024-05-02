def canSum(target,arr,memo={}):
    if(memo.get(target)):
        return memo.get(target)
    if(target==0): return True
    if(target<0): return False
    for ele in arr:
        if(canSum(target-ele,arr)==True):
            memo[target]=True
            return True
    memo[target]=False
    return False    


print(canSum(2,[3,5,7]))