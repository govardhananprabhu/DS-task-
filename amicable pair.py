"""
Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number. (A proper divisor of a number is a positive factor of that number other than the number itself.

In des
First and the last consists of two integers x and y.

Ot des
Print '1' if the following pair is amicable pair otherwise print '0'.

220 284

1

1 2

0

Exp
From sample
Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110. Sum of these is 284. Proper divisors of 284 are 1, 2, 4, 71 and 142 with sum 220.

Hint
The logic is very simple. We compare sum of the proper divisors of both numbers and compare sum for one number with other number.

H 6
T 2100
""" 
import math 
def divSum(n) :  
	result = 0
	for i in range(2, int(math.sqrt(n)) + 1) : 
		if (n % i == 0) : 
			if (i == int(n / i)) : 
				result = result + i 
			else : 
				result = result +(i + int(n / i)) 

	return (result + 1) 

def areAmicable(x, y) : 

	if (divSum(x) != y) : 
		return False
		
	return (divSum(y) == x) 
x = int(input())
y = int(input())
if (areAmicable(x, y)) : 
	print ("1") 
else : 
	print ("0") 
	
