"""Question
Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

Input description
First line has list of integers

Output description
print the value(integer)

Explanation
  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

Input
1 2 3 4 45
Output
4

Input
3 4 2 4 5 8
Output
5

Input
9 2 3 4 5 6 7 8 18 0
Output
8

Input
1 2 3 4 5
Output
5

Input
6 5 4 3 2 1
Output
-1

Hint
Run two loops. In the outer loop, pick elements one by one from left. In the inner loop, compare the picked element with the elements starting from right side.
Stop the inner loop when you see an element greater than the picked element and keep updating the maximum j-i so far.
Solution:"""
def maxIndexDiff(arr, n):
    maxDiff = -1
    for i in range(0, n):
        j = n - 1
        while(j > i):
            if arr[j] > arr[i] and maxDiff < (j - i):
                maxDiff = j - i;
            j -= 1
    return maxDiff 


arr = list(map(int,input().split()))
n = len(arr) 
maxDiff = maxIndexDiff(arr, n) 
print(maxDiff) 

