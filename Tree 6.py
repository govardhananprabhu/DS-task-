"""
Question
Construct the level order tree from the list and find the nodes which
has maximum count.

Input description
list has numbers

Output description
nodes which has max count

Input
1 2 3 4 5 5 5
Output
5

Input
1 1 1 1 1 1 
Output
1

Input
R R G G F F G
Output
G

Input
R G R G R G R G 
Output
R G

Input
1 2 3 4 5
Output
1 2 3 4 5

Hint:
Find the count of nodes which is present many times than the others.
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


def inOrder(root,i): 
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
            if(current.data==i):
                    c+=1
            current = current.right  
  
        else: 
            break
    
    ans.append(c)		

arr = input().split()
ans=[]
n = len(arr)
res=[]
for i in arr:
    if i not in res:
        res.append(i)
root = None
root = insertLevelOrder(arr, root, 0, n)
for i in res:
    inOrder(root,i)
k=max(ans)
for i in range(len(res)):
    if(k==ans[i]):
        print(res[i],end=" ")
