"""
Question
Construct the level order tree from the list and find the diagonal nodes from created
tree.


Input description
First line has list of numbers

Output description
Print each diagonals in seperate line

Explanation
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
                               1 \
                           2\     3\
                        4\    5\ 6\   7\
                     8\    9\  
                    
output:
1 3 7
2 5 6
4 9
8

Input
1 2 3 4 5
Output
1 3
2 5
4

Input
1 2 3
Output
1 3
2

Input
1 2 3 4 5 6 7 8 9
Output
1 3 7
2 5 6
4 9
8

Input
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Output
1 3 7 15
2 5 11 6 13 14
4 9 10 12
8

Input
1
Output
1


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





def diagonalPrintUtil(root, d, diagonalPrintMap):  
    if root is None: 
        return 
    try : 
        diagonalPrintMap[d].append(root.data) 
    except KeyError: 
        diagonalPrintMap[d] = [root.data] 
    diagonalPrintUtil(root.left, d+1, diagonalPrintMap) 
    diagonalPrintUtil(root.right, d, diagonalPrintMap)  
def diagonalPrint(root):   
    diagonalPrintMap = dict()  
    diagonalPrintUtil(root, 0, diagonalPrintMap) 
    for i in diagonalPrintMap:
        ans=[]
        for j in diagonalPrintMap[i]: 
            ans.append(j) 
        print(*ans) 
 
    
arr = input().split()
n = len(arr)
root = None
root = insertLevelOrder(arr, root, 0, n)
diagonalPrint(root)



