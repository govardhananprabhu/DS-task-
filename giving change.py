"""
Akash needs to buy a gift for his girfriend,he is given with N number of coins with the amount of gift K,
the cashier has to change for the amount he paid,so help akash to pick the coins which gives min change,print the min change. 

in des
First line contain integer N,size of array
Second line contain N space separated integers,denotes the coins.
Third line contain integer K,denotes the amount

ot des
Print the min change.

H=4
T=1000

5
1 2 3 4 5
10
1


3
1 3 2
4
1


6
4 3 2 5 1 7
13
1

6
11 8 4 5 1 7
13
2


4
22 44 31 11
50
5


exp
From sample
44+11=55
55-50=5
the change given by cashier is 5

Hint
Sort the arr in descending order and traverse the arr add each element and check it is greater than k, every time update the snall diff and print the diff finally.



"""
 
N=int(input())
l=list(map(int,input().split()))
K=int(input())
l.sort()
l=l[::-1]
s=0
ans=[]
for i in range(N):
    s+=l[i]
    if(s>K):
        ans.append(s-K)
        s-=l[i]
print(min(ans))
    

