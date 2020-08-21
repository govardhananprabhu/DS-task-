"""
Write a function to print spiral order traversal of a tree.
Note:tree created by binary tree formation


In des
First line contain integer N,denotes size of tree
Second line contain N space separated integers,denotes nodes of tree.

Ot des
Print the nodes in traversed order.
7
1 2 3 4 5 6 7

Exp
From sample
The tree creted will be
                 1
             2->    ->3
          4    <-5 <-6  <-7
the spiral form of level order traversal of given tree is 1 2 3 7 6 5 4

Hint
First it will print the top,then at the next row it will print from left to right,then at next right to left vice versa till the end.

H 8
T 2000

""" 
class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None
def insertLevelOrder(arr, root, i, n):  
	if i < n: 
		temp = newNode(arr[i]) 
		root = temp
		root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n) 


		root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
	return root   
def printSpiral(root): 
    if (root == None): 
        return  
    s1 = [] 
    s2 = []   
    s1.append(root)   
    while not len(s1) == 0 or not len(s2) == 0:  
        while not len(s1) == 0: 
            temp = s1[-1]  
            s1.pop()  
            print(temp.data, end = " ")   
            if (temp.right):  
                s2.append(temp.right)  
            if (temp.left): 
                s2.append(temp.left)  
        while (not len(s2) == 0): 
            temp = s2[-1]  
            s2.pop()  
            print(temp.data, end = " ")    
            if (temp.left): 
                s1.append(temp.left)  
            if (temp.right):  
                s1.append(temp.right)


N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
root = None
root = insertLevelOrder(arr, root, 0, n) 
printSpiral(root) 
