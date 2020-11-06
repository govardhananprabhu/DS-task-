"""
Given two positive numbers as strings. The numbers may be very large (may not fit in long long int), the task is to find product of these two numbers.
string len <= 50
H 7 T 2000
Tag string

In des
First line contains a space separated 2 strings s1 and s2.

Ot des
print the value

4154 51454
213739916

654154154151454545415415454 63516561563156316545145146514654
41549622603955309777243716069997997007620439937711509062916

123534 72538971
8961029243514

12345 54321
670592745

987425 8346938275498713254
8241975526684316934830950

Exp
multiply both strings

Hint
We start from last digit of second number multiply it with first number. Then we multiply second digit of second number with first number, and so on. We add all these multiplications. While adding, we put i-th multiplication shifted.

"""
def multiply(num1, num2): 
	len1 = len(num1) 
	len2 = len(num2) 
	if len1 == 0 or len2 == 0: 
		return "0"
	result = [0] * (len1 + len2) 
	i_n1 = 0
	i_n2 = 0
	for i in range(len1 - 1, -1, -1): 
		carry = 0
		n1 = ord(num1[i]) - 48
		i_n2 = 0
		for j in range(len2 - 1, -1, -1): 
			n2 = ord(num2[j]) - 48
			summ = n1 * n2 + result[i_n1 + i_n2] + carry 
			carry = summ // 10
			result[i_n1 + i_n2] = summ % 10

			i_n2 += 1
		if (carry > 0): 
			result[i_n1 + i_n2] += carry 
		i_n1 += 1 
	i = len(result) - 1
	while (i >= 0 and result[i] == 0): 
		i -= 1
	if (i == -1): 
		return "0" 
	s = "" 
	while (i >= 0): 
		s += chr(result[i] + 48) 
		i -= 1

	return s
str1,str2 = input().split()

if((str1[0] == '-' or str2[0] == '-') and
(str1[0] != '-' or str2[0] != '-')): 
	print("-", end = '') 


if(str1[0] == '-' and str2[0] != '-'): 
	str1 = str1[1:] 
elif(str1[0] != '-' and str2[0] == '-'): 
	str2 = str2[1:] 
elif(str1[0] == '-' and str2[0] == '-'): 
	str1 = str1[1:] 
	str2 = str2[1:] 
print(multiply(str1, str2)) 
