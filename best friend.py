"""
Question
Klaus needs to find eleja's best friend,klaus is m and eleja is n,best friend is the
closest num
Note:
Given two integers n and m. The problem is to find the number closest to n and divisible by m.
If there are more than one such number, then output the one having maximum absolute value. If n
is completely divisible by m, then output n only.

Input description
First line has two integers n and m 
Output description
print the closest num

Explanation
Input : n = -15, m = 6
Output : -18
Both -12 and -18 are closest to -15, but
-18 has the maximum absolute value.

Input
2 7
Output
0

Input
10 4
Output
12

Input
44 3
Output
45

Input
1 1
Output
1

Input
0 1
Output
0

Hint
We find value of n/m. Let this value be q. Then we find closest of two possibilities. One is q * m other is (m * (q + 1)) or (m * (q – 1)) depending on whether one of the given two numbers is negative or not.
"""
def closestNumber(n, m) :
	q = int(n / m) 
	n1 = m * q 
	if((n * m) > 0) : 
		n2 = (m * (q + 1)) 
	else : 
		n2 = (m * (q - 1)) 
	if (abs(n - n1) < abs(n - n2)) : 
		return n1 
	return n2 
n,m=map(int,input().split())
print(closestNumber(n, m)) 


