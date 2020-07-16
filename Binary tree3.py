"""
Question:
In your garden there is a mango tree,now it is manago season,but only right side
of tree has well grown mango,so your task is to find the count of mango which is
well grown

Input description
List has mangoes

Output description
Print the count

Explanation
Top M M M M M 
                        Top
                        /\
                       /  \
                      M  "M"
                     /\    \
                    /  \    \
                   M   M    "M"
output:
2
the double qouted M is the right side mangoes

Input
Top M M M M M M
Output
2

Input
Top M M M M M 
Output
2

Input
Top M M M M M M M M M M
Output
3

Input
Top M M M M M M M M M M M M M M M
Output
4

Input
Top M M
Output
1

Hint: count the right sided M in tree

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
        ans.append(root.data)
        max_level[0] = level 
    rightViewUtil(root.right, level+1, max_level) 
    rightViewUtil(root.left, level+1, max_level) 
  
def rightView(root): 
    max_level = [0] 
    rightViewUtil(root, 1, max_level) 
ans=[]
arr = input().split() 
n = len(arr) 
root = None
root = insertLevelOrder(arr, root, 0, n)
rightView(root)
print(len(ans)-1)
