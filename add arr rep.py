"""
Given two array A[0….n-1] and B[0….m-1] of size n and m respectively, representing two numbers such that every element of arrays represent a digit.

In des
First line contain two space separated integers N,M,denotes size of array.
Second line contain N space separated integers,denotes arr1 elements.
Third line contain M space separated integers,denotes arr2 elements.

Ot des
Print the added value.
3 3
1 2 3
2 1 4
337

4 3
9 5 4 9
2 1 4
9763

Exp
From sample
A[] = { 1, 2, 3} and B[] = { 2, 1, 4 } represent 123 and 214 respectively. The task is to find the sum of both the number. In above case, answer is 337.

Hint
The idea is to start traversing both the array simultaneously from the end until we reach the 0th index of either of the array. While traversing each elements of array, add element of both the array and carry from the previous sum. Now store the unit digit of the sum and forward carry for the next index sum. While adding 0th index element if the carry left, then append it to beginning of the number.

H 6
T 3000

"""
def calSumUtil( a , b , n , m ):  
	sum = [0] * n 
	i = n - 1
	j = m - 1
	k = n - 1
	
	carry = 0
	s = 0
	while j >= 0:  
		s = a[i] + b[j] + carry 
		sum[k] = (s % 10) 
		carry = s // 10
		
		k-=1
		i-=1
		j-=1
	while i >= 0: 
		s = a[i] + carry 
		sum[k] = (s % 10) 
		carry = s // 10
		
		i-=1
		k-=1
	
	ans = 0
	if carry: 
		ans = 10
	for i in range(n): 
		ans += sum[i] 
		ans *= 10
	
	return ans // 10
def calSum(a, b, n, m ): 
	if n >= m: 
		return calSumUtil(a, b, n, m) 
	else: 
		return calSumUtil(b, a, m, n) 

N,M=map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
n = len(a) 
m = len(b) 
print(calSum(a, b, n, m)) 

# This code is contributed by "Sharad_Bhardwaj". 
