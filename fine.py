"""
Given a date and an array of integer containing the numbers of the cars traveling on that date(an integer), the task is to calculate the total fine collected based on the following rules:

Odd numbered cars can travel on only odd dates.
Even numbered cars on only even dates.
Otherwise a car would be fined 250 Rs.

H 5 T 2000
Tag array mathematics 

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers, denotes number of cars.
Third line contains an integer date.

Ot des
Print the fine.

4
3 4 1 2
15

500

3
1 2 3
16

500

5
1 3 2 4 5
10

750

3
1 1 1
2

750

1 22 3 1 4 55 70
28

1000



Exp
Car with numbers '4' and '2' will be fined
250 each.


Hint
Start traversing the given array.
Check if the current car number and date doesn’t match i.e. one is even and other is odd or vice-versa.
If not matched charge the fine on that car number. Else, not.
Print the total fine.

"""
 
def totFine(car_num, n, date, fine) : 

	tot_fine = 0
	for i in range(n) : 
		if (((car_num[i] ^ date) & 1) == 1 ): 
			tot_fine += fine 
 
	return tot_fine
n=int(input())
car_num = list(map(int,input().split()))
date=int(input())
fine=250
print(totFine(car_num, n, date, fine)) 

