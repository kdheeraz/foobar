def merge(A,L,R):
    nL= len(L)
    nR= len(R)
    #A= [0]*(nL+nR)
    i,j,k=0,0,0

    while(i<nL and j<nR):
        if(L[i]<=R[j]):
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    while(i<nL):
        A[k]=L[i]
        i+=1
        k+=1
    while(j<nR):
        A[k]=R[j]
        j+=1
        k+=1  
    return A




def MergeSort(A):
    
    N = len(A)
    mid= N//2
    if(len(A)<2):
        return
    left = A[0:mid]
    right= A[mid:N]
    MergeSort(left)
    MergeSort(right)

    merge(A,left,right)


A=[4,2]
MergeSort(A)
print(A)