"""
Given a binary tree and an integer S, check whether there is root to leaf path wiht its sum as S.
Note:The tree created from array is by level order.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes tree nodes.
Third line contain integer S,denotes sum.

Ot des
Print 1 if there is root to leaf path with sum else 0.

3
1 2 3
2

0

3
1 2 3
4

1

5
1 2 3 4 5
8

1

5
1 2 3 4 5
7

1

5
1 2 3 4 5
9

0
Exp
From sample:
Tree = 
            1
          /   \
        2      3
S = 2
output=0
There is no root to leaf path with sum 2.

Hint
Recursively check if left or right child has path sum equal to ( number – value at current node).

H 8
T 1000
"""
class Node:  
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def hasPathSum(node, s): 

	if node is None: 
		return (s == 0) 

	else: 
		ans = 0

		subSum = s - node.data 
		

		if(subSum == 0 and node.left == None and node.right == None): 
			return True

		if node.left is not None: 
			ans = ans or hasPathSum(node.left, subSum) 
		if node.right is not None: 
			ans = ans or hasPathSum(node.right, subSum) 

		return ans 


def insertLevelOrder(arr, root, i, n):  
    if i < n: 
        temp = Node(arr[i])  
        root = temp   
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)    
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
    return root 
n=int(input())
arr=list(map(int,input().split()))
s=int(input())
root = None
root = insertLevelOrder(arr, root, 0, n)

if hasPathSum(root, s): 
	print("1") 
else: 
	print("0")  
