def bestSum(nums,target):
    if(target==0): return []
    if(target<0): return None

    finalComb=None

    for num in nums:
        rem = target - num
        remcomb = bestSum(nums,rem)

        if(remcomb!=None):
            comb = [num]+remcomb
            if(finalComb == None or len(comb)<len(finalComb)):
                finalComb = comb
    return finalComb        


print(bestSum([2,3,4,6],12))