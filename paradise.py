"""
Question
Professor needs to find the paradise number he founds it,he can able to find the path
to paradise,the paradise number is the nearest multiple of 10.

Input description
First line has integer n
Output description
print the paradise number

Input
4722
Output
4720

Input
38
Output
40

Input
10
Output
10

Input
1
Output
0

Input
0
Output
0
Hint
Let’s round down the given number n to the nearest integer which ends with 0 and store this value in a variable a.
Solution"""
def round( n ): 
	a = (n // 10) * 10
	b = a + 10
	return (b if n - a > b - n else a) 
n = int(input())
print(round(n))
