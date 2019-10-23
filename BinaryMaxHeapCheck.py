def isHeap(arr, i, n): 
    if i > int((n - 2) / 2):  
        return True
    if(arr[i]>=arr[2 * i + 1] and 
       arr[i] >= arr[2 * i + 2] and 
       isHeap(arr, 2 * i + 1, n) and
       isHeap(arr, 2 * i + 2, n)): 
        return True
      
    return False
  
if __name__ == '__main__':
    n = int(input("Enter size of array : "))
    art = []
    for i in range(n):
        a=int(input("Enter array element"+" "+str(i+1)+" - "))
        art.append(a)
    for x in range(len(art)): 
        print(str(art[x])+",", end="")   
    if isHeap(art, 0, n): 
        print("\nYes it is a MaxBinaryHeap") 
    else: 
        print("\nNo it is not a MaxBinaryHeap") 
