"""
Question
A number is termed as triangular number if we can represent it in the form of triangular
grid of points such that the points form an equilateral triangle and each row contains
as many points as the row number, i.e., the first row has one point, second row has two
points, third row has three points and so on.

Input description
First line has integer N
Output description
print yes or no

Explanation
The starting triangular numbers are 1,3 (1+2), 6 (1+2+3), 10 (1+2+3+4).

Input
1
Output
yes

Input
2
Output
no

Input
3
Output
yes

Input
6
Output
yes

Input
11
Output
no
Hint
We start with 1 and check if the number is equal to 1. If it is not, we add 2
to make it 3 and recheck with the number. We repeat this procedure until the sum
remains less than or equal to the number that is to be checked for being triangular.
Solution:"""
def isTriangular(num):
	if (num < 0): 
		return False

	sum, n = 0, 1

	while(sum <= num): 
	
		sum = sum + n
		if (sum == num): 
			return True
		n += 1

	return False
n = int(input())
if (isTriangular(n)): 
	print("yes") 
else: 
	print("no")  
