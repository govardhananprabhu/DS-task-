"""
Given a large number N and the task is to check if any permutation of a large number is divisible by 8.
string len<= 10
H 5 T 2000
Tag string math

In des
First line contains only one string

Ot des
print yes or no

31462708
Yes

10101
No

75
No

241422
Yes

78645228
Yes

Exp
Many of permutation of number N like 
34678120, 34278160 are divisible by 8. 

Hint
The approach is to generate all permutations of the number N and check if(N % 8 == 0) and return true if any of the permutations is divisible by 8.

"""
def solve(n, l):  
	if l < 3: 
		if int(n) % 8 == 0: 
			return True
		n = n[::-1] 

		
		if int(n) % 8 == 0: 
			return True
		return False
	hash = 10 * [0] 
	for i in range(0, l): 
		hash[int(n[i]) - 0] += 1; 
	for i in range(104, 1000, 8): 
		dup = i 
		freq = 10 * [0] 
		freq[int(dup % 10)] += 1; 
		dup = dup / 10
		freq[int(dup % 10)] += 1; 
		dup = dup / 10
		freq[int(dup % 10)] += 1; 
		
		dup = i 
		if (freq[int(dup % 10)] > 
			hash[int(dup % 10)]): 
			continue; 
		dup = dup / 10; 
		
		if (freq[int(dup % 10)] > 
			hash[int(dup % 10)]): 
			continue; 
		dup = dup / 10
		
		if (freq[int(dup % 10)] > 
			hash[int(dup % 10)]): 
			continue; 
		
		return True
	return False
number = input()
l = len(number) 
if solve(number, l):
    print("Yes")
else:
    print("No")
