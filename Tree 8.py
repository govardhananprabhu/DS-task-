"""
Question
Construct the level order tree from the list and find the left diagonal values
of tree.

Input description
First line has list of numbers

Output description
left diagonal node

Explanation
1 2 3 4 5 7 8 9
                            *1
                            /\
                           *2  3
                          / \  /\
                         *4  5 6  7
                         /\
                        *8 9

the * highlighted values are left diagonal values of tree
1 2 4 8

Input
1 2 3 4 5
Output
1 2 4

Input
1 2 3
Output
1 2

Input
1 2 3 4 5 6 7 8 9 10 11 12 13 14
Output
1 2 4 8

Input
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 23
Output
1 2 4 8 17

Input
1 3 2 5 4 6 8 7 5 6 4 7 3 44 33 556 6 3 2 1 66 77 55 4 33333 2 1 456  6
Output
1 3 5 7 556

Hint:
Traverse through the left side nodes only,print all the traversed nodes.
solution:"""
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


def Postorder(root): 
  
    if root:
        ans.append(root.data)
        Postorder(root.left)
    
    
            
    

arr = input().split()
n = len(arr)
ans=[]
res=[]
root = None
root = insertLevelOrder(arr, root, 0, n)
Postorder(root)

print(*ans)


