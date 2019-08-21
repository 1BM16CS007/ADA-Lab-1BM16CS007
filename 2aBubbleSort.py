
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
def kthSmallest(arr, n, k): 
    bubbleSort(arr)  
    return arr[k-1] 
if __name__=='__main__': 
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr) 
    k = 2
    print("K'th smallest element is", 
          kthSmallest(arr, n, k)) 



