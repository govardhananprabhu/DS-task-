"""
Question
Given an unsorted array of positive integers, find the number of triangles that can be formed with three different array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any of the two values (or sides) must be greater than the third value (or third side).

Input description
First line has size of array N
Second line has array elemenents
Output description
print the count

Explanation
Input: arr= {4, 6, 3, 7}
Output: 3
Explanation: There are three triangles 
possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. 
Note that {3, 4, 7} is not a possible triangle.

Input
4
1 3 2 5
Output
0

Input
4
3 2 5 1
Output
0

Input
6
1 4 6 9 3 5
Output
6

Input
3
1 2 3
Output
0

Input
4
4 6 3 7
Output
3
Hint
The brute force method is to run three loops and keep track of the number of triangles possible so far. The three loops select three different values from an array. The innermost loop checks for the triangle property which specifies the sum of any two sides must be greater than the value of the third side
Solution:"""
def findNumberOfTriangles(arr, n): 
	count = 0
	for i in range(n): 
		for j in range(i + 1, n):  
			for k in range(j + 1, n): 
				if (arr[i] + arr[j] > arr[k] and
					arr[i] + arr[k] > arr[j] and
					arr[k] + arr[j] > arr[i]): 
					count += 1
	return count
N=int(input())
arr = list(map(int,input().split())) 
size = len(arr) 
print(findNumberOfTriangles(arr, size)) 
 
