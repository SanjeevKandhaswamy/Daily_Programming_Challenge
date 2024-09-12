"""
Problem : Merge Two Sorted Arrays
You are given two sorted arrays arr1 of size m and arr2 of size n. 
Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). 
The elements in arr1 should be merged first, followed by the elements of arr2, 
resulting in both arrays being sorted after the merge.

Input :
Two sorted integer arrays arr1 of size m and arr2 of size n.
Example : 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

Output :
Both arr1 and arr2 should be sorted after the merge. Since you cannot use extra space, the final result will be reflected in arr1 and arr2.
Example:
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
"""

def sort_array(arr1, arr2):
    i = len(arr1) - 1
    j = len(arr2) - 1
    k = len(arr1) + len(arr2) - 1

    merged = [0] * (len(arr1) + len(arr2))

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            merged[k] = arr1[i]
            i -= 1
        else:
            merged[k] = arr2[j]
            j -= 1
        k -= 1

    while i >= 0:
        merged[k] = arr1[i]
        i -= 1
        k -= 1

    while j >= 0:
        merged[k] = arr2[j]
        j -= 1
        k -= 1

    arr1[:] = merged[:len(arr1)]
    arr2[:] = merged[len(arr1):]

    return arr1, arr2

# Driver Code
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

sort_array(arr1, arr2)

print("arr1:", arr1)
print("arr2:", arr2)
