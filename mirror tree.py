"""
Given a Binary Tree, convert it into its mirror.
Note: Tree created by level order and print by inorder.

In des
First line contains integer N,denotes the count of nodes.
Second line contains N space separated integers,denotes nodes of tree.

Ot des
Print the original image of original tree in first line.
Print the mirror image of original tree in second line.

3
1 2 3

2 1 3
3 1 2

5
1 2 3 4 5

4 2 5 1 3
3 1 5 2 4

4
1 3 2 4

4 3 1 2
2 1 3 4

1
1

1
1

6
1 3 2 4 6 5

4 3 6 1 5 2
2 5 1 6 3 4

Input:
      1
    /  \
   2    3
Output: 3 1 2
Explanation: The tree is
   1    (mirror)  1
 /  \    =>      /  \
2     3         3    2
The inorder of mirror is 3 1 2

Hint
Print the mirror image of the tree,reverse of tree.

""" 
class newNode: 
	def __init__(self,data): 
		self.data = data 
		self.left = self.right = None

def mirror(node): 

	if (node == None): 
		return
	else: 

		temp = node 
		mirror(node.left) 
		mirror(node.right) 
		temp = node.left 
		node.left = node.right 
		node.right = temp 
 

def insertLevelOrder(arr, root, i, n):  
	if i < n: 
		temp = newNode(arr[i]) 
		root = temp 
		root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n) 


		root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
	return root  
def inOrder(root): 
	if root != None: 
		inOrder(root.left) 
		ans.append(root.data) 
		inOrder(root.right)
N=int(input())
arr=list(map(int,input().split()))
n = len(arr)
ans=[]
root = None
root = insertLevelOrder(arr, root, 0, n) 
inOrder(root)
print(*ans)
mirror(root) 
inOrder(root)
print(*ans[N:])

