"""
Given a value n, find out the largest palindrome number which is product of two n digit numbers.

In des
First line contain integer N,denotes the range of digits.

Ot des
Print the palindrome.

2
9009

3
906609

Exp
From sample
9009 is the largest number which is product of two 
2-digit numbers. 9009 = 91*99.

Hint
1) Find a lower limit on n digit numbers. For example, for n = 2, lower_limit is 10.
2) Find an upper limit on n digit numbers. For example, for n = 2, upper_limit is 99.
3) Consider all pairs of numbers where ever number lies in range [lower_limit, upper_limit]

H 6
T 3000
"""
def larrgestPalindrome(n): 

	upper_limit = 0) 
	for i in range(1, n+1): 
	
		upper_limit =upper_limit * 10
		upper_limit =upper_limit + 9 
	lower_limit = 1 + upper_limit//10

	max_product = 0 
	for i in range(upper_limit,lower_limit-1, -1): 
	
		for j in range(i,lower_limit-1,-1): 
			product = i * j 
			if (product < max_product): 
				break
			number = product 
			reverse = 0 
			while (number != 0): 
			
				reverse = reverse * 10 + number % 10
				number =number // 10 
			if (product == reverse and product > max_product): 
				max_product = product 
		
	
	return max_product 

N = int(input())
print(larrgestPalindrome(n)) 
