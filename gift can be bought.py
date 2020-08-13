"""
Akash needs to buy a gift for his girfriend,he is given with N number of coins with the amount of gift K,
the cashier has no changes to give,so help akash to pick the coins which's sum exactly
equals to K,print yes if akask can buy else no.

in des
First line contain integer N,size of array
Second line contain N space separated integers,denotes the coins.
Third line contain integer K,denotes the amount

ot des
Print yes or no.

H=4
T=1000

5
1 3 2 4 5
10
yes


3
1 3 2
0
no


1
1
1
yes

3
25 10 5
30
yes

3
5 3 2
4
no



exp
We can use one coin of 25 cents and one of 5 cents,
its sum is exactly equals to amount no change needed
output yes. 

Hint
Sort the arr in descending order and traverse the arr add each element and check its equal to k every time if yes print yes,if it exceeds print no.



"""
 
N=int(input())
l=list(map(int,input().split()))
K=int(input())
l.sort()
l=l[::-1]
s=0
for i in range(N):
    s+=l[i]

    if(s==K):
        print('yes')
        break
    if(s>K):
        s-=l[i]
    if(i+1==N):
        print('no')

