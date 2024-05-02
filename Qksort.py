from MRSort import MergeSort
import time
def partition(A,S,E):
    pivot = A[E]
    pIndex= S
    for i in range(S,E):
        if(A[i]<=pivot): # if A[i] is less than pivot than swap A[i] and A[pIndex]
            A[i],A[pIndex]=A[pIndex],A[i]
            pIndex+=1
    A[E],A[pIndex]=A[pIndex],A[E]   

    return pIndex   
 
def QkSort(A,S,E):
    if(S>=E):
        return
    pIndex = partition(A,S,E)
    QkSort(A,S,pIndex-1)
    QkSort(A,pIndex+1,E) 

A=[7,3,1,6,2,8,5,4]
B=[7,3,1,6,2,8,5,4]



A1=time.time_ns()
QkSort(A,0,7)

print(time.time_ns()-A1)

B1=time.time_ns()
MergeSort(B)

print(time.time_ns()-B1)

