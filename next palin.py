"""
Given a number, find the next smallest palindrome larger than this number.

H 6
T 1000
Tag yahoo string

In des
First line contains integer N.

Ot des
Print the next palindrome.

123

131

23545

23632

999

1001

111

121

234

242

Exp
For example, if the input number is 23545, the output should be 23632. And if the input number is 999, the output should be 1001.

Hint


""" 
def generateNextPalindromeUtil (num, n) : 
	mid = int(n/2 )  
	leftsmaller = False
	i = mid - 1
	j = mid + 1 if (n % 2) else mid  
	while (i >= 0 and num[i] == num[j]) : 
		i-=1
		j+=1
 
	if ( i < 0 or num[i] < num[j]): 
		leftsmaller = True
	while (i >= 0) : 
	
		num[j] = num[i] 
		j+=1
		i-=1
	
	if (leftsmaller == True) : 
	
		carry = 1
		i = mid - 1
		if (n%2 == 1) : 
		
			num[mid] += carry 
			carry = int(num[mid] / 10 ) 
			num[mid] %= 10
			j = mid + 1
		
		else: 
			j = mid 
 
		while (i >= 0) : 
		
			num[i] += carry 
			carry = num[i] / 10
			num[i] %= 10
			num[j] = num[i]
			j+=1
			i-=1 
def generateNextPalindrome(num, n ) :  
	if( AreAll9s( num, n ) == True) : 
	
		print( "1",end="") 
		for i in range(1, n): 
			print( "0",end="" ) 
		print( "1",end="")  
	else: 
	
		generateNextPalindromeUtil ( num, n ) 
		printArray (num, n) 
def AreAll9s(num, n ): 
	for i in range(1, n): 
		if( num[i] != 9 ) : 
			return 0
	return 1
def printArray(arr, n): 

	for i in range(0, n): 
		print(int(arr[i]),end="") 
	print() 
 
N=input()
num=[]
for i in N:
    num.append(int(i))
n = len(num) 
generateNextPalindrome( num, n ) 
