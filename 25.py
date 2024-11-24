import numpy as np

array = np.random.rand(4, 5) * 10
subtracted_array = array - 2
print("\nArray after subtracting 2 from each element:\n", subtracted_array)


num_dimensions = array.ndim
print("\nNumber of dimensions:", num_dimensions)


shape_of_array = array.shape
print("Shape of array:", shape_of_array)


flattened_array = array.flatten()
print("\nFlattened array:\n", flattened_array)

sliced_array = array[:2, ::2]
print("\nSliced array (first 2 rows and alternate columns):\n", sliced_array)

min_element = np.min(array)
print("\nMinimum element of array:", min_element)

cumulative_sum = np.cumsum(array, axis=1)
print("\nCumulative sum along each row:\n", cumulative_sum)


sorted_array = np.sort(array, axis=1)
print("\nArray sorted row-wise:\n", sorted_array)

def merge_sort(arr):
    """Recursive merge sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

         
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

       
        while j < len(R):
            arr[k] = R[j]
            
