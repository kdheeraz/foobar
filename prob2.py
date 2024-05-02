def solution(l):
    SUM = sum(l)
    sorted_l = sorted(l,reverse=True)
    if(len(l)==0):
        return 0
    if(len(l)==1):
        if(not l[0]%3):
            return l[0]
        else:
            return 0
    if(SUM % 3!=0):
        sub_sum=sum(sorted_l)
        for i in range(len(sorted_l)-1,-1,-1):
            if((sub_sum-sorted_l[i])%3==0):
                sorted_l.pop(i)
                return int(''.join(map(str, sorted_l)))
        sorted_l.pop()
        return solution(sorted_l)
    else:
        return int(''.join(map(str, sorted_l)))