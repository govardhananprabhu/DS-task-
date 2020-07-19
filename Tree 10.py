"""
Question
Construct the level order tree from the list and find the parent node of the given
value in created tree.If not founded print -1

Input description
First line has list of numbers

Output description
parent node

Explanation
1 2 3 4 5 6 7 8 9
5
                            1
                            /\
                           2   3
                          / \  /\
                         4  5 6  7
                         /\
                        8 9

output: 2

Input
1 2 3 4 5
3
Output
1

Input
1 2 3
2
Output
1

Input
1 2 3 4 5 6 7 8 9 10 11 12 13 14
14
Output
7

Input
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 23
12
Output
6

Input
1 3 2 5 4 6 8 7 5 6 4 7 3 44 33 556 6 3 2 1 66 77 55 4 33333 2 1 456  6
1
Output
-1

Hint:
Traverse through the left,right side nodes then check data is equal to k,
if yes print the previous value and end the traversal.
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


def tra(root,k,parent): 
  
    if root:
        if root.data==k:
                print(parent)
                return 
        else:
                tra(root.left,k,root.data)
                tra(root.right,k,root.data)

        
    
            
    

arr = input().split()
k=input()
n = len(arr)
ans=[]
root = None
root = insertLevelOrder(arr, root, 0, n)
tra(root,k,-1)




