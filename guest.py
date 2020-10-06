"""
Consider a big party where a log register for guest’s entry and exit times is maintained. Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.

H 8
T 2000
Tag accolite array

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integer, denotes the arrival of guest.
Third line contains N space separated integer, denotes the departure of guest.

Ot des
Print the maximum guest and time with space separation

5
1 2 9 5 5
4 5 12 9 12

3 5

3
1 4 2
2 5 7

2 2

4
1 2 3 4
4 3 2 1

1 1

5
2 1 4 6 11
3 11 4 6 5
2 2

2
2 2
2 2
2 2

Exp
From sample:
First guest in array arrives at 1 and leaves at 4, 
second guest arrives at 2 and leaves at 5, and so on.
There are maximum 3 guests at time 5.  


Hint
The idea is to consider all events (all arrivals and exits) in sorted order. Once we have all events in sorted order, we can trace the number of guests at any time keeping track of guests that have arrived, but not exited.
"""
def findMaxGuests(arrl, exit, n):
	arrl.sort();
	exit.sort();
	guests_in = 1;
	max_guests = 1;
	time = arrl[0];
	i = 1;
	j = 0;
	while (i < n and j < n):
		if (arrl[i] <= exit[j]):
	
			guests_in = guests_in + 1;
			if(guests_in > max_guests):
		
				max_guests = guests_in;
				time = arrl[i];
			i = i + 1; 
	
		else:
			guests_in = guests_in - 1;
			j = j + 1;
	
	print(max_guests,time)

N=int(input())
arrl = list(map(int,input().split()))
exit = list(map(int,input().split()))
n = len(arrl);
findMaxGuests(arrl, exit, n);


