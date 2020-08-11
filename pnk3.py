"""
Docter founded that for the age of given integer N,the drops needed to cure a patient
is count of 1s in binary representation of given N.


Exp
Binary representation of 6 is 110 and has 2 set bits

In des
First line contain integer N,denotes the value

Ot des
Print the count of drops

Hint
Print the count of 1s in binary value of given N.
T=1000

H=4
bit

"""
def countSetBits(n): 
	count = 0
	while (n): 
		count += n & 1
		n >>= 1
	return count 
i = 9
print(countSetBits(i)) 
 
