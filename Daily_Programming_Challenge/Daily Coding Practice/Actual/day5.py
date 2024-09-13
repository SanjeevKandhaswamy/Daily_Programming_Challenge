"""
Problem : Find the Leaders in an Array
You are given an integer array arr of size n. An element is considered a leader if it is greater than all the elements to its right. Your task is to find all such leader elements in the array.

Input :
An integer array arr of size n.
Example : 
arr = [16, 17, 4, 3, 5, 2]

Output :
Return an array containing all the leader elements in the order in which they appear in the original array.
Example:
Leaders: [17, 5, 2]
"""

def find_leaders(arr):
    leaders = []
    max_from_right = float('-inf')
    
    for num in reversed(arr):
        if num > max_from_right:
            leaders.append(num)
            max_from_right = num


    print(f"Leaders : {leaders[::-1]}")

# Driver Code
arr = [16,17,4,3,5,2]
find_leaders(arr)