"""
Question
Construct the level order tree from the list and find the left child node of the given
node from created tree.If the node is the last node then print it.


Input description
First line has list of numbers

Output description
Print given node with its left node.

Explanation
1 2 3 4 5 6 7 8 9
2
                            1
                            /\
                           2   3
                          / \  /\
                         4  5 6  7
                         /\
                        8 9

output:2 4

Input
1 2 3 4 5
3
Output
3

Input
1 2 3
1
Output
1 2

Input
1 2 3 4 5 6 7 8 9 10 11 12 13 14
6
Output
6 12

Input
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 23
3
Output
3 6

Input
1
1
Output
1

Hint:
Traverse through the nodes if k is founded then print the left node of k.
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


def tra(root,k): 
  
    if root:
        if root.data==k:
                ans.append(root.data)
                
                if root.left:
                    root=root.left
                    ans.append(root.data)
               
                   

     
        else:
                tra(root.left,k)
                tra(root.right,k)
    
    
            
    

arr = input().split()
k=input()
n = len(arr)
ans=[]
root = None
root = insertLevelOrder(arr, root, 0, n)
tra(root,k)

print(*ans)
