"""
Given three array of size N, id, time, profit, find the maximum profit obtained a person from id's.
The Condition is only one work is done at a time, in the array there may be many offers at same time.   

H 7
T 2000
Tag Accolite array

In des
First line contains integer N.
Second line contains N space separated integers, denotes id's.
Third line contains N space separated integers, denotes time.
Second line contains N space separated integers, denotes profit.

Ot des
Print id's
4
a b c d
4 1 1 1
20 10 40 30

a c

5
a b c d e
2 1 2 1 1
100 19 27 25 15

a d

3
a d e
1 2 3
10 20 30

a d e

2
a c
1 1
30 31

c

6
a c e r t q
2 1 3 2 2 2
11 32 42 16 24 90

q c e 
Exp
From sample:
The id a has maximum profit at time 4,similarly c has at time 1.

Hint
Find the different timings present in array and then find the max profit of each time and which id holds it.
"""
n=int(input())
id=input().split()
deadline=list(map(int,input().split()))
pro=list(map(int,input().split()))
a=[]
res=[]
for i in deadline:
    if i not in a:
        a.append(i)
for i in a:
    c=0
    for j in range(n):
        if(deadline[j]==i):
            if(pro[j]>c):
                c=pro[j]
    res.append(c)
for i in res:
    print(id[pro.index(i)],end=" ")
            
            
    
