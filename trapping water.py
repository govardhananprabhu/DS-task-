"""
Question
Given an array arr[] of N non-negative integers representing height of blocks at
index i as Ai where the width of eachblock is 1. Compute how much water can be
trapped in between blocks after raining.

Input description
First line has list of integers

Output description
print theq uantity in integer

Explanation
arr=[2,0,1,2]
output:2+1=3

Input
3 0 0 3
Output
6

Input
3 0 2 0 4
Output
7

Input
0 1 0 2 1 0 1 3 2 1 2 1
Output
6

Input
1
Output
0

Input
1 1 1
Output
0

HINT
The idea is to traverse every array element and find the highest bars on left and right sides.
Take the smaller of two heights. The difference between the smaller height and height of the
current element is the amount of water that can be stored in this array element

Solution:"""
def maxWater(arr, n) :  
	res = 0;  
	for i in range(1, n - 1) : 
		left = arr[i]; 
		for j in range(i) : 
			left = max(left, arr[j]); 
		right = arr[i]; 
		
		for j in range(i + 1 , n) : 
			right = max(right, arr[j]);
		res = res + (min(left, right) - arr[i]); 

	return res; 


if __name__ == "__main__" : 

	arr = list(map(int,input().split()))
	n = len(arr); 
	
	print(maxWater(arr, n)); 
     
