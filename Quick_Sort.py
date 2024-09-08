# arr = [3,2,1,8,54,90,-378,3243,1]
# def swap (arr,i,j):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp
#     def pivot (arr,start,end):
#         pivot = arr[end]
#         i = start-1
#         for j in range (start,end):
#             if arr[0] < pivot:
#                 i = i+1
#                 swap(arr,i,j)
#                 i=i+1
#                 swap(arr,i,end)
#                 return i
#             def Quick_Sort(arr,start,end):
#                 if(start<end):
#                     pivot = pivot(arr,start,end)
#                     Quick_Sort(arr,start,end)
#                     Quick_Sort(arr,start,pivot-1)
#                     Quick_Sort(arr,pivot+1,end)
#                     Quick_Sort(arr,0,len(arr)-1)
#                     print(arr)

def partition(array, low, high):
 
   
    pivot = array[high]
 
    i = low - 1
 
   
    for j in range(low, high):
        if array[j] <= pivot:
 
            
            i = i + 1
 
           
            (array[i], array[j]) = (array[j], array[i])
 
  
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    
    return i + 1
 

 
 
def quickSort(array, low, high):
    if low < high:
 
        
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
 
      
        quickSort(array, pi + 1, high)
 
 
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)