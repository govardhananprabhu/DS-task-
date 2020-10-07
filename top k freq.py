"""
Given an array of n numbers. Your task is to read numbers from the array and keep at-most K numbers at the top (According to their decreasing frequency) every time a new number is read. We basically need to print top k numbers sorted by frequency when input stream has included k distinct elements, else need to print all distinct elements sorted by frequency.

H 7
T 2500
Tag accolite array

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers, denotes array elements.
Third line contains integer K, denotes the size for top elements 

Ot des
Print the k top elements for every element in array.


5
5 2 1 3 2
4

5 2 5 1 2 5 1 2 3 5 2 1 3 5

5
5 2 1 3 4
4

5 2 5 1 2 5 1 2 3 5 1 2 3 4

3
1 3 2
2

1 1 3 1 2

3
1 3 2
3
1 1 3 1 2 3 

4
1 1 1 1
4

1 1 1 1
Exp
From sample:
After reading 5, there is only one element 5 whose frequency is max till now.
so print 5.
After reading 2, we will have two elements 2 and 5 with the same frequency.
As 2, is smaller than 5 but their frequency is the same so we will print 2 5.
After reading 1, we will have 3 elements 1, 2 and 5 with the same frequency,
so print 1 2 5.
Similarly after reading 3, print 1 2 3 5
After reading last element 2 since 2 has already occurred so we have now a
frequency of 2 as 2. So we keep 2 at the top and then rest of the element
with the same frequency in sorted order. So print, 2 1 3 5.

Hint
The idea is to store the top k elements with maximum frequency. To store them a vector or an array can be used. To keep the track of frequencies of elements create a HashMap to store element-frequency pair. Given a stream of numbers, when a new element appears in the stream update the frequency of that element in HashMap and put that element at the end of the list of K numbers (total k+1 elements) now compare adjacent elements of the list and swap if higher frequency element is stored next to it.

"""
def kTop(a, n, k):  
	top = [0 for i in range(k + 1)]  
	freq = {i:0 for i in range(k + 1)} 
	for m in range(n):  
		if a[m] in freq.keys(): 
			freq[a[m]] += 1
		else: 
			freq[a[m]] = 1
		top[k] = a[m] 

		i = top.index(a[m]) 
		i -= 1
		
		while i >= 0: 
			if (freq[top[i]] < freq[top[i + 1]]): 
				t = top[i] 
				top[i] = top[i + 1] 
				top[i + 1] = t 
			elif ((freq[top[i]] == freq[top[i + 1]]) and (top[i] > top[i + 1])): 
				t = top[i] 
				top[i] = top[i + 1] 
				top[i + 1] = t 
			else: 
				break
			i -= 1
		i = 0
		while i < k and top[i] != 0: 
			print(top[i],end=" "), 
			i += 1
	print
N=int(input())
arr = list(map(int,input().split()))
k=int(input())
n = len(arr) 
kTop(arr, n, k) 
