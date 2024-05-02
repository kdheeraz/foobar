# import sys
# sys.setrecursionlimit(3333)
# dp_map={}
# def solution(n):
#     if(isinstance(n,str)):
#         n= int(n)
#     if(n==0):
#         return 1
#     if(n==1):
#         return 0
#     if(n==2):
#         return 1
#     if n in dp_map:
#         return dp_map[n]
#     elif(n%2==0):
#         dp_map[n] = 1 + solution(int(n//2))
#     elif(n%2==1):
#         dp_map[n] = 1+ min( solution(n-1),solution(n+1))
 
#     return dp_map[n]  

def solution(n):
    n = int(n)
    count = 0
    while n != 1:
        if n ==2:
            n=n-1
            count+=1
        elif (n%2==0):
            count=count+1
            n=n//2
        elif(n%2 !=0):
            n += 1
            count += 1
        else:
            n    
    return count    

print(solution(str(10**309 - 1)))    

print(solution(str(15)))    
