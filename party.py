"""
Question
Tony stark  has a party tonight only his friends can be invited,his friends are y and tony is x,
you need to find y is power of x.If yes print 1 else 0.

Input description
First line has integers x and y

Output description
print 1 or 0

Explanation
Input:  x = 10, y = 1
Output: True
x^0 = 1

Input
10 1
Output
1
Input
10 1000
Output
1
Input
10 1001
Output
0
Input
1 1
Output
1
Input
2 64
Output
1
Hint
A simple solution is to repeatedly compute powers of x. If a power becomes equal to y, then y is a power, else not.
Solution:"""
def isPower (x, y): 
	if (x == 1): 
		return (y == 1) 
	pow = 1
	while (pow < y): 
		pow = pow * x
	return (pow == y)
x,y=map(int,input().split())
if(isPower(x,y)): 
	print(1) 
else: 
	print(0)
