"""
Given a number n and a value k, turn off the k’th bit in n. Please note that k = 1 means the rightmost bit.

H 5 T 2000
Tag bit

In des
Fist line contains 2 space separated integers n, k, denotes number rightmost bit.

Ot des
Print the value after turn off

15 1
14

14 1
144/

15 2
13

15 3
11

15 4
7

Exp
The rightmost bit was already off, so no change.

Hint
The idea is to use bitwise <<, & and ~ operators. Using expression "~(1 << (k – 1))“, we get a number which has all bits set, except the k’th bit. If we do bitwise & of this expression with n, we get a number which has all bits same as n except the k’th bit which is 0.

"""
def turnOffK(n,k):
	if (k <= 0): 
		return n 
	return (n & ~(1 << (k - 1))) 

n, k = map(int,input().split())
print(turnOffK(n, k)) 
