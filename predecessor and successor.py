"""
You need to create tree from the array using level order. You need to find the inorder successor and predecessor of a given key. In case, if the either of predecessor or successor is not found print -1.

In des
First line contain integer N,size of array.
Second line contain N space separated integers, dennotes nodes of tree.
Third line contains integer,denotes key to find successor and predecessor

Ot des
Print space separated successor and predecessor if possible else print -1.

50 30 70 20 40 60 80
65

60 70

7
50 20 60 10 30 55 70
55

50 60

7
50 20 60 10 30 55 70
45
30 50

7
50 20 60 10 30 55 70
75
70 -1

7
50 20 60 10 30 55 70
5
-1 10
Exp
From sample
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80  

Predecessor is 60
Successor is 70


Hint
Check if the current node is smaller than the given key for predecessor and for successor, check if it is greater than the given key . If it is greater than the given key then, check if it is smaller than the already stored value in successor then, update it . At last, get the predecessor and successor stored in q(successor) and p(predecessor).

H 8
T 2000

Tag Ola cabs tree

""" 
class Node: 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None
def findPreSuc(root, key): 
	if root is None: 
		return
	if root.key == key: 

		if root.left is not None: 
			tmp = root.left 
			while(tmp.right): 
				tmp = tmp.right 
			findPreSuc.pre = tmp 
		if root.right is not None: 
			tmp = root.right 
			while(temp.left): 
				tmp = tmp.left 
			findPreSuc.suc = tmp 

		return

	if root.key > key : 
		findPreSuc.suc = root 
		findPreSuc(root.left, key) 

	else: 
		findPreSuc.pre = root 
		findPreSuc(root.right, key) 
def insert(node , key): 
	if node is None: 
		return Node(key) 

	if key < node.key: 
		node.left = insert(node.left, key) 

	else: 
		node.right = insert(node.right, key) 

	return node 
def insertLevelOrder(arr, root, i, n):  
    if i < n: 
        temp = Node(arr[i])  
        root = temp   
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)   
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
    return root

n=int(input())
arr=list(map(int,input().split()))
root = None
root = insertLevelOrder(arr, root, 0, n)
key = int(input())
findPreSuc.pre = None
findPreSuc.suc = None

findPreSuc(root, key) 

if findPreSuc.pre is not None: 
	print(findPreSuc.pre.key,end=" ") 

else: 
	print(-1,end=" ")

if findPreSuc.suc is not None: 
	print(findPreSuc.suc.key,end=" ") 
else: 
	print(-1,end=" ")
