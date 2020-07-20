"""
Question
Construct the level order tree from the list and find the boundary nodes from created
tree.


Input description
First line has list of numbers

Output description
Print boundary nodes.

Explanation
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
                              *1
                     *2                *3
                *4        5          6       *7
              *8  *9  *10   *11   *12  *13 *14  *15
                    
output: 1 2 4 8 9 10 11 12 13 14 15 7 3
* highlighted values are boundary nodes.

Input
1 2 3 4 5
Output
1 2 4 5 3

Input
1 2 3
Output
1 2 3

Input
1 2 3 4 5 6 7 8 9
Output
1 2 4 8 9 5 6 7 3

Input
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 23
Output
1 2 4 8 17 23 9 10 11 12 13 14 15 7 3

Input
1
Output
1

Hint:
Traverse through left nodes and then through leaf nodes and finally right nodes,print
the traversed nodes
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


def printLeaves(root): 
    if(root): 
        printLeaves(root.left) 
        if root.left is None and root.right is None: 
            ans.append(root.data), 
  
        printLeaves(root.right)  
def printBoundaryLeft(root): 
      
    if(root): 
        if (root.left): 
            ans.append(root.data) 
            printBoundaryLeft(root.left) 
          
        elif(root.right): 
            ans.append(root.data) 
            printBoundaryLeft(root.right) 
          
       
def printBoundaryRight(root): 
      
    if(root): 
        if (root.right): 
            
            printBoundaryRight(root.right) 
            ans.append(root.data) 
          
        elif(root.left): 
            printBoundaryRight(root.left) 
            ans.append(root.data) 
  
 
def printBoundary(root): 
    if (root): 
        ans.append(root.data)  
        printBoundaryLeft(root.left) 
        printLeaves(root.left) 
        printLeaves(root.right) 
        printBoundaryRight(root.right) 
    
    
            
    

arr = input().split()
n = len(arr)
ans=[]
root = None
root = insertLevelOrder(arr, root, 0, n)
printBoundary(root)
print(*ans)


