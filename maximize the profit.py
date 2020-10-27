"""
Given an array seats[] where seat[i] is the number of vacant seats in the ith row in a stadium for a cricket match. There are N people in a queue waiting to buy the tickets. Each seat costs equal to the number of vacant seats in the row it belongs to. The task is to maximize the profit by selling the tickets to N people.

H 6 T 1500

Tag array mathematics

In des
First line contains integer N, size of array.
Second line contains N space separated integers, denotes array elements.
Third line contains integer K,denotes the people in queue.

Ot des
print the profit

3
2 1 1
3

4

5
2 3 4 5 1
6

22

4
1 2 3 4
2
7

6
11 2 1 3 33 2 17
4
126

3
2 1 3
1
3


Exp
Person 1: Sell the seat in the row with
2 vacant seats, seats = {1, 1, 1}
Person 2: All the rows have 1 vacant
seat each, seats[] = {0, 1, 1}
Person 3: seats[] = {0, 0, 1}

Hint
In order to maximize the profit, the ticket must be for the seat in a row which has the maximum number of vacant seats and the number of vacant seats in that row will be decrement by 1 as one of the seats has just been sold. All the persons can be sold a seat ticket until there are vacant seats.


"""
def maxProfit(seats, k, n) : 
	pq = []; 
	for i in range(k) : 
		pq.append(seats[i]);  
	pq.sort(reverse = True); 
	profit = 0; 
	c = 0; 
	while (c < n) : 
		pq.sort(reverse = True); 
		top = pq[0];  
		pq.pop(0); 
		if (top == 0) : 
			break; 
		profit = profit + top; 
		pq.append(top - 1); 
		c += 1; 
	
	return profit; 

n=int(input())
seats = list(map(int,input().split()))
k = len(seats); 
n1 = int(input()) 
print(maxProfit(seats, k, n1)); 

