"""
Given a array of N numbers with that data create a binary tree and print its diagonal sums.

H 8
T 1000
Tag accolite tree

In des
First line contains integer N, size of array.
Second line contains N space separated integers, denotes array elements.

Ot des
Print the every sum of diagonal with space separation.

5
3 2 1 5 4

8 6 1 

4
2 1 3 4

9 1

6
3 22 1 43 23 11

68 35

2
2 1

2 1

10
22 1 32 45 65 43 21 123 22 19
287 65 19

Exp
From sample:
first diagonal has 3+5=8,second has 2+4=6 and third has 1.

Hint
The idea is to keep track of vertical distance from top diagonal passing through the root. We increment the vertical distance we go down to next diagonal. 
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
def diagonalSumUtil(root, vd, diagonalSum) :
 
    if(not root): 
        return
         
    if vd not in diagonalSum:
        diagonalSum[vd] = 0
    diagonalSum[vd] += root.data 
    diagonalSumUtil(root.left, vd + 1, 
                          diagonalSum) 
    diagonalSumUtil(root.right, vd,
                       diagonalSum)  
def diagonalSum(root) :
    diagonalSum = dict() 
     
    diagonalSumUtil(root, 0, diagonalSum) 
     
    for it in diagonalSum:
        print(diagonalSum[it], end = " ")
diagonalSum(root)
