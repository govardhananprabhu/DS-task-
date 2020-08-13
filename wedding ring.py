"""
Barath needs to buy a wedding ring,he has N number of coines,the amount of ring is given as K,find he has enough money to buy or not,if yes print the balance after he bought else
print how much he required more to buy.

in des
First line contain integer N,size of array
Second line contain N space separated integers,denotes the coins.
Third line contain integer K,denotes the amount

ot des
Print the amount.

H=4
T=1000

5
1 2 3 4 5
10
5


5
1 2 3 4 5
20
5


5
3 2 5 6 7
4
19


1
1
1
0


4
22 44 31 11
50
58


exp
From sample
1+2+3+4+5=15
15-10=5
the remaining amount he has is 5

1+2+3+4+5=15
20-15=5
the required amount he need more to buy is 5

Hint
Find the sum of list and compare it with amount K to find that he bought or not.


"""
 
N=int(input())
l=list(map(int,input().split()))
K=int(input())
s=sum(l)
if(s>=K):
    print(s-K)
else:
    print(K-s)
    

