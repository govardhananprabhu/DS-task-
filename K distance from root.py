"""
Given a Binary Tree of size N and an integer K. Print all nodes that are at distance k from root (root is considered at distance 0 from itself). Nodes should be printed from left to right. If k is more that height of tree, nothing should be printed.
Note tree created by level order

In des
First line contain integer N, denotes number of nodes
Second line contain N space separated integers, denotes nodes in tree.
Third line contain integer K, denotes the distance.

Ot des
Print the nodes with space sepated, which are at the distance k.
3
1 2 3
1
2 3 

5
1 2 3 4 5
1
2 3

8
1 3 2 4 5 7 9 123
3
123

16
1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 0
3
8 7 6 5 4 3 2 1

5
1 2 3 4 5
2

4 5
From sample:
the 4 and 5 nodes are at distance 2

Hint
Traverse from the root and print the nodes at distance K.

H 7
T 1000




"""
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def insertLevelOrder(arr, root, i, n):  
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)   
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
    return root 
def printKDistant(root, k): 
	
	if root is None: 
		return
	if k == 0: 
		print(root.data,end=" ") 
	else: 
		printKDistant(root.left, k-1) 
		printKDistant(root.right, k-1) 
N=int(input())
arr=list(map(int,input().split()))
K=int(input())
root = None
root = insertLevelOrder(arr, root, 0, N)

printKDistant(root, K) 
