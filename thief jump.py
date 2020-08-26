"""
A thief trying to escape from a jail has to cross N walls each with varying heights. He climbs X feet every time. But, due to the slippery nature of those walls, every times he slips back by Y feet.  Now the task is to calculate the total number of jumps required to cross all walls and escape from the jail.

In des
First line contains three space separated integers X, Y, N.
Then in the next line are N space separated values denoting the heights ( Ht[] ) of the walls.

Ot des
For each test case in a new line print the total number of jumps.

10 1 2
11 11

4

10 1 1
5

1

4 1 5
6 9 11 4 5

12

10 1 4
11 10 10 9

5

10 1 5
11 10 10 9 9

6
exp
From sample:
He needs to make 2 jumps for first wall and 2 jumps for second wall


Hint
The solution is quite simple if the height of wall is less than or equal to x, only one jump in that wall is required else we can calculate it by height of wall-(climb up-climb down) and get the jumps required.

H 6
T 2000
""" 
def jumpcount(x, y, n, height): 
	jumps = 0

	for i in range(n): 
		if (height[i] <= x): 
			jumps += 1
			continue
		h = height[i] 
		while (h > x): 
			jumps += 1
			h = h - (x - y) 
		jumps += 1
	return jumps 
x,y,n=map(int,input().split())
height = list(map(int,input().split())) 
print(jumpcount(x, y, n, height)) 


