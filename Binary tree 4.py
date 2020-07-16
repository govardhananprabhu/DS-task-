"""
Question:
You are given with a list,construct binary tree and find the count of numbers
present in both left and right side.


Input description
List has numbers

Output description
Print the count

Explanation
Top 1 2 3 4 5 
                        Top
                         /\
                       '1' '2'
                       /   /\
                     '3'   4 '5'
if extra digit added
6
then tree look's like
                        Top
                         /\
                       '1' '2'
                       /\   /\
                     '3' 4 5 '6'

output:
4
the double qouted numbers are the left side and right side numbers


Input
Top 2 3 4 5 6
Output
4

Input
Top 1 2 3 4 5 6 7 8 9 10
Output
6

Input
Top 1 2 3 4 5 6 7
Output
5

Input
Top 1 2 3 4 5
Output
4

Input
Top 1 2
Output
2

Hint: Find the right sided and left sided numbers and print their count.

Solution:"""
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

def rightViewUtil(root, level, max_level): 
    if root is None: 
        return
    if (max_level[0] < level):
        right.append(root.data)
        max_level[0] = level 
    rightViewUtil(root.right, level+1, max_level) 
    rightViewUtil(root.left, level+1, max_level) 
  
def rightView(root): 
    max_level = [0] 
    rightViewUtil(root, 1, max_level)

def leftViewUtil(root, level, max_level):
    if root is None: 
        return 
    if (max_level[0] < level):
        if root.data not in right:
            left.append(root.data) 
        max_level[0] = level  
    leftViewUtil(root.left, level + 1, max_level) 
    leftViewUtil(root.right, level + 1, max_level) 
  
def leftView(root): 
    max_level = [0] 
    leftViewUtil(root, 1, max_level) 
left=[]
right=[]
arr = input().split() 
n = len(arr) 
root = None
root = insertLevelOrder(arr, root, 0, n)
rightView(root)
leftView(root)
print(left,right)
print(len(left)+len(right)-1)
