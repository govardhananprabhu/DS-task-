"""
Question
In an apple tree there are two colour's of apples,find the count of green and red
apple in tree."Tree created by level order".

Input description
list has apples

Output description
count of red and green apples

Input
R R R G G
Output
3 2

Input
R R R R R R R
Output
7 9

Input
R R R R R R R G G G G G G
Output
7 6

Input
R G R G R G R G G
Output
4 5

Input
R G
Output
1 1

Hint:
Find the count of R snd G.
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


def inOrder(root,n): 
    current = root  
    stack = [] 
    done = 0 
    c=0
    while True:
        if current is not None:  
            stack.append(current) 
          
            current = current.left  
        elif(stack): 
            current = stack.pop()
            if(current.data=='R'):
                    c+=1
            current = current.right  
  
        else: 
            break
    print(c,n-c)		

arr = input().split()
c=0
n = len(arr)
root = None
root = insertLevelOrder(arr, root, 0, n)
inOrder(root,n)
