"""
Akash needs to buy a gift for his girfriend,he is given with N number of coins with the amount of gift K,
the cashier has no changes to give,so help akash to pick the coins which's sum exactly
equals to K,print the minimum count of coins taken out.Note a coin can taken out many times. 

in des
First line contain integer N,size of array
Second line contain N space separated integers,denotes the coins.
Third line contain integer K,denotes the amount

ot des
Print the min count

H=6
T=2000

5
1 3 2 4 5
10
2



3
13 4 12
21
3


1
1
1
1

3
25 10 5
30
2


4
9 6 5 1
11
2



exp
Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

Hint
Sort in descending order and traverse each coin,add same coins till it does not extends K,stop when the traversed coins sum
equals to k and print the count of coin traversed.


"""
 

import sys 

def minCoins(coins, m, V): 
	if (V == 0): 
		return 0
 
	res = sys.maxsize 
 
	for i in range(0, m): 
		if (coins[i] <= V): 
			sub_res = minCoins(coins, m, V-coins[i]) 

			if (sub_res != sys.maxsize and sub_res + 1 < res): 
				res = sub_res + 1

	return res 
N=int(input())
coins = list(map(int,input().split())) 
m = len(coins) 
V = int(input())
print(minCoins(coins, m, V)) 

