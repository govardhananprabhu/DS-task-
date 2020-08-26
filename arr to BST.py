"""
Given a sorted array. Write a program that creates a Balanced Binary Search Tree using array elements. If there are N elements in array, then floor(n/2)'th element should be chosen as root and same should be followed recursively.

In des
The first line contains integer N(size of array).
The second line contains N space separated integers of A[].

Ot des
Print the preorder traversal of constructed BST.


7
1 2 3 4 5 6 7

4 2 1 3 6 5 7

3
1 2 3

2 1 3

4
1 2 3 4

3 2 1 4

2
1 2

2 1

1
1

1
Exp
From sample: A Balanced BST
     2
   /  \
  1    3

Hint
Get the Middle of the array and make it root.Recursively do same for left half and right half.Get the middle of left half and make it left child of the root created in step 1.Get the middle of right half and make it right child of theroot created in step 1.

H 8
T 2000

"""
class Node: 
	def __init__(self, d): 
		self.data = d 
		self.left = None
		self.right = None
def sortedArrayToBST(arr): 
	
	if not arr: 
		return None 
	mid = (len(arr)) // 2
	root = Node(arr[mid]) 
	root.left = sortedArrayToBST(arr[:mid])  
	root.right = sortedArrayToBST(arr[mid+1:]) 
	return root 
def preOrder(node): 
	if not node: 
		return
	
	print(node.data,end=" ") 
	preOrder(node.left) 
	preOrder(node.right) 
N=int(input())
arr = list(map(int,input().split()))
root = sortedArrayToBST(arr)  
preOrder(root) 

