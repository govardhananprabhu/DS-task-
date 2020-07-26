"""
Question
Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

Input description:
First line has integer input

Output description:
Print the possible's in integer

Explanation:
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input
1
Output
1

Input
2
Output
2

Input
3
Output
4

Input
4
Output
7

Input
5
Output
13
Hint:
Calculate the possibleties to reach the dest with three possible steps 1,2,3.

Solution:"""
def printCountRec(dist):
	if dist < 0: 
		return 0
		
	if dist == 0: 
		return 1
	return (printCountRec(dist-1) +
			printCountRec(dist-2) +
			printCountRec(dist-3)) 
dist = int(input())
print(printCountRec(dist))
