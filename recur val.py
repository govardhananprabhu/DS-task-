"""
Given a fraction, find a recurring sequence of digits if exists, otherwise, print -1.

H 5 T 1500
Tag math

In des
First line contains 2 space separated integers N, D, denotes numerator and denominator.

Ot des
Print the sequence else -1.

8 3
6

50 22
27

11 2
-1

23 4
-1

12 5
-1

Exp
8/3 = 2.66666666.......

Hint
Find the quotient value with decimal values and check any recurring occurs.

"""
def fractionToDecimal(numr, denr):
	res = "" 
	mp = {}
	rem = numr % denr
	while ((rem != 0) and (rem not in mp)):
		mp[rem] = len(res)
		rem = rem * 10
		res_part = rem // denr
		res += str(res_part)
		rem = rem % denr
	
	if (rem == 0):
		return ""
	else:
		return res[mp[rem]:]
numr, denr = map(int,input().split())
res = fractionToDecimal(numr, denr)

if (res == ""):
	print("-1")
else:
	print(res)
