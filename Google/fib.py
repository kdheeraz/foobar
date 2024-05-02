def getFib(n,memo={}):
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(memo.get(n)):
        return memo.get(n)
    else:
        temp_f= getFib(n-1,memo)+getFib(n-2,memo)
        memo[n]=temp_f
    print(memo)    
    return memo[n]  


print(getFib(7,{}))

    
    
            