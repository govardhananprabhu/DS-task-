"""
In a daily share trading, a buyer buys shares in the morning and sells it on the same day. If the trader is allowed to make at most 2 transactions in a day, whereas the second transaction can only start after the first one is complete (Sell->buy->sell->buy). Given stock prices throughout the day, find out the maximum profit that a share trader could have made.

H 6 T 2500
Tag accolite mathematics

In des
First line contain integer N,denotes size of array.
Second line contains N space separated integers, denotes price.

Ot des
Print the max profit

7
2 30 15 10 8 25 80
100

3
3 5 7
4

5
11 3 12 66 5
63

3
10 11 12
2

7
11 33 22 44 66 77 99
99

6
10 22 5 75 65 80
87

Exp
From sample:
Trader earns 87 as sum of 12 and 75,Buy at price 10, sell at 22, buy at 5 and sell at 80

Hint
The maximum difference between two elements such that larger element appears after the smaller number.
"""
def maxProfit(price,n): 
	profit = [0]*n  
	max_price=price[n-1] 
	
	for i in range( n-2, 0 ,-1): 
		
		if price[i]> max_price: 
			max_price = price[i] 
		profit[i] = max(profit[i+1], max_price - price[i]) 	 
	min_price=price[0] 
	
	for i in range(1,n): 
		
		if price[i] < min_price: 
			min_price = price[i] 	 
		profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price)) 
		
	result = profit[n-1] 
	
	return result
N=int(input())
price = list(map(int,input().split()))
print(maxProfit(price, len(price))) 
