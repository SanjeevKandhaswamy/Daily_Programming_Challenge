"""
You are given an unsorted array of integers and a positive integer K. Your task is to find the Kth largest element in the array. 
The Kth largest element is the element that would appear in the Kth position if the array were sorted in descending order.

You need to implement a function that returns this Kth largest element without explicitly sorting the entire array.

Example
arr = [3, 2, 1, 5, 6, 4]
k = 2
Output: 5
"""

import heapq

def find_kth_largest(arr,k):
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    for num in arr[k:]:
        if num>min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap,num)
    return min_heap[0]

#driver code
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(arr,k))