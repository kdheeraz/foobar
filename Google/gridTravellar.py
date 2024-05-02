def gridTraveller(m,n,memo={}):
    if(m==0 or n==0): return 0
    if(m==1 and n==1): return 1
    if(memo.get(f"{m},{n}")):
        return memo.get(f"{m},{n}")
    else:
        memo[f"{m},{n}"] = gridTraveller(m-1,n,memo)+gridTraveller(m,n-1,memo)
        return  memo[f"{m},{n}"]   
print(gridTraveller(100,100,{}))
    