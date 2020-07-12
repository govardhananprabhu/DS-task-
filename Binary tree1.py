"""
Question:
You are given with two list, construct binary tree with the elements in the list,
find the common nodes of the trees.Common node means they should be in the same
side

Input description
The first and second line has the numbers

Output description
print the common nodes with sides if not print no

Test cases
Input
9 8 10 7 15
5 4 8 3 9 3
Output
no

Input
5 6 4 3 2
7 6 4 1 9
Output
4 left

Input
1 2 3 4 5 6 7
5 1 2 3 4 6 7
Output
6 right 7 right

Solution:"""
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return
            return self.right.findval(lkpval)
        else:
            ans.append(self.data)


L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
ans=[]
root1 = Node(L1[0])
root2 = Node(L2[0])

for i in range(1,len(L1)):
    root1.insert(L1[i])
for i in range(1,len(L2)):
    root2.insert(L2[i])
if len(L1)>len(L2):
    for i in L2:
        root1.findval(i)
else:
    for i in L1:
        root2.findval(i)
res=[]
for i in ans:
    if(i==L1[0] and i==L2[0]):
        res.append(str(i)+" root")
    elif(i>L1[0] and i>L2[0]):
        res.append(str(i)+' right')
    elif(i<L1[0] and i<L2[0]):
        res.append(str(i)+' left')
if(len(res)==0):
    print("no")
else:
    print(*res)
        
