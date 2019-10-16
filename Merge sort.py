#Implement merge sort algorithm
def Merge (L, R, A):
    nl = len(L)
    nr = len(R)

    #initialize values
    i = j = k = 0

    #Keep sorting and merging until one of the arrays is fully sorted
    while (i<nl and j<nr):
        if L[i] <= R[j]:
            A[k] = L[i]
            i=i+1
        else:
            A[k] = R[j]
            j=j+1
        k=k+1

    #check if any of the array still contains elements
    #only one of these loops will run
    while (i<nl):
        A[k]=L[i]
        i=i+1
        k=k+1
    while (j<nr):
        A[k] = R[j]
        j=j+1
        k=k+1



def MergeSort (A):
    n=len(A)

    #Check if the array has less than one element
    if (n < 2):
        return
    mid = int(n/2)

    #Divide the array based on the mid point
    left = A[:mid]
    right = A[mid:]

    #Keep dividing each array till you get an array of one element
    MergeSort(left)
    MergeSort(right)

    #Run the merge function to sort and merge each array
    Merge(left, right, A)


#items = [20, 8, 19, 56, 23, 83, 41, 23, 53]
items = [0, 1.5, 50, 5]
MergeSort(items)
print (items)
