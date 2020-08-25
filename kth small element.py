"""
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

In des
First line contains an integer N denoting size of the array.
Second line contains N space separated integer denoting elements of the array.
Third line of the contains an integer K.

Ot des
print the kth smallest element in a new line.

6
7 10 4 3 20 15
3

7

5
7 10 4 20 15
4

15

Exp
From sample
3rd smallest element in the given array is 7.

Hint
A simple solution is to sort the given array using sorting algorithm and return the element at index k-1 in the sorted array.

H 5
T 2000

"""
def kthSmallest(arr, n, k):   
    arr.sort() 
    return arr[k-1] 
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
k = int(input())
print(kthSmallest(arr, n, k)) 
  
