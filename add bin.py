"""
Question
Assume you are hacker now,hih=gher officials needs your help to hack the computer
which has the acces to disable bomb,the problem is find a integer which is the addition
of two binary value.print the int value.

Input description
First line has two binary value
Output description
print the int value

Explanation
Input:  a = "11", b = "1"
Output: "100" 
Input
101 1000
Output
13
Input
11 11
Output
6
Input
1111 1111
Output
30
Input
111 111
Output
14
Input
100 100
Output
8
Hint
The idea is to start from last characters of two strings and compute digit sum one by one. If sum becomes more than 1, then store carry for next digits.

"""
def add_binary_nums(x, y): 
		max_len = max(len(x), len(y)) 

		x = x.zfill(max_len) 
		y = y.zfill(max_len) 
		result = '' 
		carry = 0
		for i in range(max_len - 1, -1, -1): 
			r = carry 
			r += 1 if x[i] == '1' else 0
			r += 1 if y[i] == '1' else 0
			result = ('1' if r % 2 == 1 else '0') + result 
			carry = 0 if r < 2 else 1

		
		if carry !=0 : result = '1' + result 

		return result.zfill(max_len) 

a,b=input().split()
print(int(add_binary_nums(a,b),2))
