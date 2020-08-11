"""
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.

Exp
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
For first value is 1,the value is 1 if decreases and if increases value is previous ones value.

H
Traverse the input price array. For every element being visited, traverse elements on left of it and increment the span value of it while elements on the left side are smaller.

Hard 6

In des
First line contain integer N denotes size of array
Second line contains N space separated integers,denotes the price.
Ot des
print N space separated value


"""
def calculateSpan(price, n, S): 
	S[0] = 1
 
	for i in range(1, n, 1): 
		S[i] = 1 

		j = i - 1
		while (j>= 0) and (price[i] >= price[j]) : 
					S[i] += 1
					j -= 1

def printArray(arr, n): 

	for i in range(n): 
		print(arr[i], end = " ")
N=int(input())
price = list(map(int,input().split()))
n = len(price) 
S = [None] * n 
calculateSpan(price, n, S) 
printArray(S, n) 

