"""
Question
Your teacher given a question and also he/she said that who solve it first will be
rewarded,so the question is to find the addition of two fraction.

Input description
First line has two integers num1 and num2
Second line  has two integers den1 and den2
Output description
print the  addition of fraction.
Explanation
Input:  1/2 + 3/2
Output: 2/1

Input
1 1
1 1
Output
2 / 1
Input
2 3
1 3
Output
3 / 1
Input
1 1
4 3
Output
7 / 12
Input
2 2
2 2
Output
2 / 1
Input
3 2
4 2
Output
7 / 4

Hint
Find a common denominator by finding the LCM (Least Common Multiple) of the two denominators.
Change the fractions to have the same denominator and add both terms.
Reduce the final fraction obtained into its simpler form by dividing both numerator and denominator by there largest common factor.
Solution:"""
def gcd(a, b): 
	if (a == 0): 
		return b; 
	return gcd(b % a, a); 

def lowest(den3, num3): 
	common_factor = gcd(num3, den3); 

	den3 = int(den3 / common_factor); 
	num3 = int(num3 / common_factor); 
	print(num3,"/",den3); 

def addFraction(num1, den1, num2, den2):  
	den3 = gcd(den1, den2); 

	den3 = (den1 * den2) / den3; 

 
	num3 = ((num1) * (den3 / den1) +
			(num2) * (den3 / den2)); 

	lowest(den3, num3); 

num1,num2=map(int,input().split())
den1,den2=map(int,input().split())
addFraction(num1, den1, num2, den2) 


