"""
hard 6
Given an array, print the Next Smaller Element (NSE) for every element. The Smaller smaller Element for an element
x is the first smaller element on the right side of x in array. Elements for
which no smaller element exist (on right side), consider next smaller element as -1.

I des
First line contain integer N,size of array
Second line contain N space separated integers,denotes array elements.

O des
Print the current value with its next smaller value in each line

Exp
For any array, rightmost element always has next smaller element as -1.
For an array which is sorted in increasing order, all elements have next smaller element as -1.
Element       NSE
   4      -->   2
   8      -->   5
   5      -->   2
   2      -->   -1
   25     -->   -1

4
2 1 4 3
2 -- 1
1 -- -1
4 -- 3
3 -- -1


2
2 3
2 -- -1
3 -- -1

3
1 2 3
1 -- -1
2 -- -1
3 -- -1

5
4 8 5 2 25
4 -- 2
8 -- 5
5 -- 2
2 -- -1
25 -- -1

1
1
1 -- -1
2000
Hint
Use two loops: The outer loop picks all the elements one by one. The inner loop looks for the first smaller element for the element picked by outer loop. If a smaller element is found then that element is printed as next, otherwise -1 is printed.

"""
def printNSE(arr): 

	for i in range(0, len(arr), 1): 

		next = -1
		for j in range(i + 1, len(arr), 1): 
			if arr[i] > arr[j]: 
				next = arr[j] 
				break
			
		print(str(arr[i]) + " -- " + str(next)) 
N = int(input())
arr = list(map(int,input().split())) 
printNSE(arr) 
 
