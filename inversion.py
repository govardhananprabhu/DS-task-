"""
Question
Dr.Strange wants to create robots,he has array of positive integers,the count of robot
he can create is equal to count of inversion from array.  
Note:
Inversion Count for an array indicates – how far (or close) the array is from being
sorted. If array is already sorted then inversion count is 0. If array is sorted in
reverse order that inversion count is the maximum.Formally speaking, two elements
a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Input description
First line has list of integers

Output description
print the count

Explanation
Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8,4), (4,2),(8,2), (8,1), (4,1), (2,1).

Input
1 3 2 4 5 4 1
Output
7

Input
1 2 3 4 5 1
Output
4

Input
1 2 3 4 5
Output
0

Input
4 3 5 2 9
Output
4

Input
0 1 0 1 0 1
Output
3

Hint
Traverse through the array and for every index find the number of smaller elements on its right side of the array. This can be done using a nested loop. Sum up the counts for all index in the array and print the sum
Solution:"""
def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 
   
arr = list(map(int,input().split()))
n = len(arr) 
print(getInvCount(arr, n)) 
