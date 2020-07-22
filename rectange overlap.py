"""
Given two rectangles, find if the given two rectangles overlap or not.
Note that a rectangle can be represented by two coordinates,top left and bottom
right. So mainly we are given following four coordinates.
l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.

Input description
four coordinate

Output description
If overlap's print yes or no

Input
1 2
1 2
1 2
1 2
Output
no

Input
1 2
2 2
1 4
0 2
Output
no

Input
1 2
2 3
0 0
1 2
Output
no

Input
1 2
2 2
1 1
2 2
Output
no

Input
0 10
10 0
5 5
15 0
Output
yes


Solution:"""
class Point: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 
 
def doOverlap(l1, r1, l2, r2): 
	if(l1.x >= r2.x or l2.x >= r1.x): 
		return False 
	if(l1.y <= r2.y or l2.y <= r1.y): 
		return False

	return True
ans=[]
for i in range(4):
    l=[]
    x,y=map(int,input().split())
    l.append(x)
    l.append(y)
    ans.append(l)
    
l1 = Point(ans[0][0],ans[0][1]) 
r1 = Point(ans[1][0],ans[1][1]) 
l2 = Point(ans[2][0],ans[2][1]) 
r2 = Point(ans[3][0],ans[3][1]) 

if(doOverlap(l1, r1, l2, r2)):
    print("yes") 
else:
    print("no") 

