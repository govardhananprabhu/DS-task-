"""
Given a array of N numbers with that data create a binary tree and print the vertical of tree.
Example
                 3
              2     5
            1    4
output of the tree is
1 
2 
3 4 
5

H 8
T 1000
Tag accolite tree

In des
First line contains integer N, size of array.
Second line contains N space separated integers, denotes array elements.

Ot des
Print the every vertical values with space separation in each line.


5
3 2 5 1 4

1 
2 
3 4 
5

3
3 2 1
1 
2 
3

5
2 1 4 3 5
1 
2 3 
4 
5

8
3 2 4 7 6 5 1 2
1 
2 
3 5 
4 6 
7

7
1 2 3 4 5 6 7
1 
2 
3 
4 
5 
6 
7

Exp
From sampla:
                 3
              2     5
            1    4
output of the tree is
1 
2 
3 4 
5
Hint
We need to check the Horizontal Distances from the root for all nodes. If two nodes have the same Horizontal Distance (HD), then they are on the same vertical line.
"""
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


N=int(input())
l=list(map(int,input().split()))
root = Node(l[0])
for i in range(1,N):
    root.insert(l[i])
def getVerticalOrder(root, hd, m):
    if root is None:
        return
    try:
        m[hd].append(root.data)
    except:
        m[hd] = [root.data]
    getVerticalOrder(root.left, hd-1, m)
    getVerticalOrder(root.right, hd+1, m)
def printVerticalOrder(root):
    m = dict()
    hd = 0
    getVerticalOrder(root, hd, m)
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i,end=" ")
        print(sep="\n")
printVerticalOrder(root)
 
