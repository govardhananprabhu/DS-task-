"""
Question
Given an integer n, write a function that returns count of trailing zeroes in n!.

Input description
First line has integer n
Output description
print the count

Explanation
Input: n = 5
Output: 1 
Factorial of 5 is 120 which has one trailing 0.


Input: n = 20
Output: 4
Factorial of 20 is 2432902008176640000 which has
4 trailing zeroes.

Input: n = 100
Output: 24

Hint
A simple method is to first calculate factorial of n, then count trailing 0s in the result (We can count trailing 0s by repeatedly dividing the factorial by 10 till the remainder is 0).
Solution"""
def findTrailingZeros(n): 
	count = 0

	i=5
	while (n/i>=1): 
		count += int(n/i) 
		i *= 5

	return int(count) 
n = int(input())
print(findTrailingZeros(n)) 
 
