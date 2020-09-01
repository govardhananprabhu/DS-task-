"""
Given a binary tree and two node values your task is to find the distance between them.Note the tree created from array is by level order.

In des
First line contain integer N,denotes size of array.
Second line contains N space separated integers, denotes nodes of tree.
Third line contains two integer values, which's distance should be founded.

Ot des
Print the distance else -1.

5
1 2 3 4 5
2 3

2

3
1 2 3
2 3
2

3
1 2 3
1 3
1

3
1 2 3
1 2
1

8
1 2 3 4 5 6 7 8
4 8
1


Exp
From sample:
                    1
                2       3
            4      5
The distance betweem 2 and 3 is 2.


Hint
The distance between two nodes can be obtained in terms of lowest common ancestor. Following is the formula.

Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)

H 8
T 2000

Tag Ola cabs, tree

"""
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None 
def LCA(root, n1, n2):  
	if root is None: 
		return None
 
	if root.data == n1 or root.data == n2: 
		return root 
	left = LCA(root.left, n1, n2) 
	right = LCA(root.right, n1, n2) 

	if left is not None and right is not None: 
		return root 
	if left: 
		return left 
	else: 
		return right 

def findLevel(root, data, d, level): 
	if root is None: 
		return
	if root.data == data: 
		d.append(level) 
		return

	findLevel(root.left, data, d, level + 1) 
	findLevel(root.right, data, d, level + 1) 
def findDistance(root, n1, n2): 
	
	lca = LCA(root, n1, n2) 
	d1 = [] 
	d2 = [] 
	if lca: 
		findLevel(lca, n1, d1, 0)  
		findLevel(lca, n2, d2, 0) 
		return d1[0] + d2[0] 
	else: 
		return -1
def insertLevelOrder(arr, root, i, n):  
    if i < n: 
        temp = Node(arr[i])  
        root = temp   
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)   
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
    return root

n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
root = None
root = insertLevelOrder(arr, root, 0, n)
 

print(findDistance(root, a, b)) 
 
