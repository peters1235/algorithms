import sys
import random
def merge(A,p,q,r):
     
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(sys.maxint)
    R.append(sys.maxint)

    i = 0
    j = 0 
    for k in range(p,r+1): 
        if(L[i]<= R[j]): 
            A[k] = L[i]
            i+=1
        else: 
            A[k] = R[j]
            j+=1

def mergeWithoutWatch(A,p,q,r):
    L=A[p:q+1]
    R=A[q+1:r+1]
    i=j=0;
    for k in range(p,r+1):
        if(i>=len(L)):
            A[k] = R[j]
            j+=1
        elif (j>= len(R)):
            A[k] = L[i]
            i+=1
        elif(L[i] <= R[j]):
            A[k] = L[i]
            i+=1;
        elif (R[j] <= L[i]):
            A[k] = R[j]
            j+=1
            
def mergeSort(A,p,r):
    if(p<r):
        q=(p+r)/2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        mergeWithoutWatch(A,p,q,r)
    
###################################
def insertKey(A,j):
    key = A[j]
    i= j-1
    while(i>=0 and A[i]>=key):
        A[i+1] = A[i]
        i -= 1
    A[i+1] = key
    
def insertSort(A):
    for j in range(1,len(A)):
        insertKey(A,j)
        
def recurInsertSort(A):
    if(len(A) >1):
        recurInsertSort(A[0:-1])
    insertKey(A,len(A)-1)
    print(A)
     
###############################
def inAscenOrder(A):
    for i in range(0,len(A)-1):
        if(A[i] > A[i+1]):
            return False
    return True

A = random.sample(xrange(100), 10)

print (A)
#mergeSort(A,0,9)
#insertSort(A)
recurInsertSort(A)
print inAscenOrder(A)
print(A)

